# 🖼️ apply_watermark

A Python command-line script to apply a **tiled watermark** over images in a folder.

---

## 📦 Requirements

- Python 3.8 or higher
- [Pillow](https://pypi.org/project/Pillow/)
- [Typer](https://pypi.org/project/typer/)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to use

```bash
python main.py \
 --input ./in \
 --output ./out \
 --error ./error \
 --watermark ./watermark.png \
 --opacity 0.8 \
 --spacing 50 \
 --watermark-scale 0.2 \
 --max-width 800 \
 --max-height 800
```

---

## ⚙️ Parameters

| Parameter                  | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| `--input`, `-i`            | Path to the input folder with the images                         |
| `--output`, `-o`           | Path to the output folder for processed images                   |
| `--error`, `-e`            | Folder to move images that failed during processing              |
| `--watermark`, `-w`        | Path to the `.png` watermark image with transparency             |
| `--opacity`, `-p`          | Watermark opacity (0.0 to 1.0). Example: `0.3` for 30%           |
| `--spacing`, `-s`          | Spacing in pixels between each repeated watermark tile           |
| `--watermark-scale`, `-ws` | Scale of the watermark image (e.g. `0.5` = 50%, `2.0` = 200%)    |
| `--max-width`              | Maximum width of the output image (use `0` to disable resizing)  |
| `--max-height`             | Maximum height of the output image (use `0` to disable resizing) |

---

## 🖼️ Example

```bash
python main.py \
 --input ./in \
 --output ./out \
 --error ./error \
 --watermark ./watermark.png \
 --opacity 0.8 \
 --spacing 50 \
 --watermark-scale 0.2 \
 --max-width 1024 \
 --max-height 768
```

This command:

- Applies `watermark.png` with 80% opacity
- Scales the watermark to 20% of its original size
- Adds 50px spacing between each tile
- Resizes the image to a maximum of `1024x768`
- Moves failed images to the `error` folder

---

## 🧼 Behavior

- Input images are deleted after successful processing
- Failed images are moved to the error folder (if defined)

---

## 🧪 Logs

The script prints logs to the terminal:

- `INFO`: Progress and resizing messages
- `ERROR`: Reading, writing, or format errors

---

## 🧊 Tip

Use transparent `.png` images as watermarks for best results.
