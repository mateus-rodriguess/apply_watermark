import typer
import os
from PIL import Image
import logging
import shutil


def apply_image_watermark(
    input_folder: str,
    output_folder: str,
    error_folder: str | None,
    watermark_path: str,
    opacity: float = 0.3,
    max_width: int = 0,
    max_height: int = 0,
    spacing: int = 0,
    watermark_scale: float = 1.0,
):
    os.makedirs(output_folder, exist_ok=True)
    if error_folder:
        os.makedirs(error_folder, exist_ok=True)

    try:
        watermark = Image.open(watermark_path).convert("RGBA")
    except Exception as error:
        logging.error(f"Error opening watermark: {error}")
        raise SystemExit(1)

    if watermark_scale != 1.0:
        new_wm_width = int(watermark.width * watermark_scale)
        new_wm_height = int(watermark.height * watermark_scale)
        watermark = watermark.resize(
            (new_wm_width, new_wm_height), Image.Resampling.LANCZOS
        )

    wm_width, wm_height = watermark.size

    if opacity < 1:
        alpha = watermark.split()[3]
        alpha = alpha.point(lambda p: int(p * opacity))
        watermark.putalpha(alpha)

    for filename in os.listdir(input_folder):
        filepath = os.path.join(input_folder, filename)

        try:
            base_image = Image.open(filepath).convert("RGBA")

            if max_width > 0 or max_height > 0:
                orig_width, orig_height = base_image.size
                ratio = min(
                    (max_width / orig_width) if max_width > 0 else 1,
                    (max_height / orig_height) if max_height > 0 else 1,
                )
                if ratio < 1:
                    new_size = (int(orig_width * ratio), int(orig_height * ratio))
                    base_image = base_image.resize(new_size, Image.Resampling.LANCZOS)
                    logging.info(f"{filename} resized to {new_size}")

            watermark_layer = Image.new("RGBA", base_image.size, (0, 0, 0, 0))

            step_x = wm_width + spacing
            step_y = wm_height + spacing

            for y in range(0, base_image.height, step_y):
                for x in range(0, base_image.width, step_x):
                    watermark_layer.paste(watermark, (x, y), watermark)

            watermarked_image = Image.alpha_composite(
                base_image, watermark_layer
            ).convert("RGB")

            output_path = os.path.join(output_folder, filename)

            ext = os.path.splitext(filename)[1].lower()
            save_params = {}
            if ext in [".jpg", ".jpeg"]:
                save_params["quality"] = 85
                save_params["optimize"] = True
            elif ext == ".png":
                save_params["optimize"] = True

            watermarked_image.save(output_path, **save_params)
            os.remove(filepath)

            logging.info(f"Processed: {filename}")

        except Exception as error:
            logging.error(f"Error processing {filename}: {error}")
            if error_folder:
                error_path = os.path.join(error_folder, filename)
                try:
                    shutil.move(filepath, error_path)
                    logging.info(f"File {filename} moved to error folder.")
                except Exception as move_error:
                    logging.error(
                        f"Error moving {filename} to error folder: {move_error}"
                    )


def main(
    input_folder: str = typer.Option(
        ..., "--input", "-i", help="Input folder with images"
    ),
    output_folder: str = typer.Option(
        ..., "--output", "-o", help="Output folder for processed images"
    ),
    error_folder: str = typer.Option(
        None, "--error", "-e", help="Folder for images with processing errors"
    ),
    watermark: str = typer.Option(
        "watermark.png", "--watermark", "-w", help="Path to the watermark image"
    ),
    opacity: float = typer.Option(
        0.3, "--opacity", "-p", help="Watermark opacity (0 to 1)"
    ),
    max_width: int = typer.Option(
        0, "--max-width", help="Maximum width for resizing (0 to ignore)"
    ),
    max_height: int = typer.Option(
        0, "--max-height", help="Maximum height for resizing (0 to ignore)"
    ),
    spacing: int = typer.Option(
        50, "--spacing", "-s", help="Spacing between watermark tiles (in pixels)"
    ),
    watermark_scale: float = typer.Option(
        1.0,
        "--watermark-scale",
        "-ws",
        help="Watermark scale (e.g. 0.5 = 50%, 2.0 = 200%)",
    ),
):
    apply_image_watermark(
        input_folder,
        output_folder,
        error_folder,
        watermark,
        opacity,
        max_width,
        max_height,
        spacing,
        watermark_scale,
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Example:
    # python main.py --input ./in --output ./out --error ./error --watermark ./watermark.png --opacity 0.8 --spacing 50 --watermark-scale 0.2 --max-width 500 --max-height 500
    typer.run(main)
