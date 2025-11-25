# HEIC to JPEG converter

A python script to convert images in HEIC as JPEG.


## Getting started

### Prerequisites

- Python 3.12

### Installation

1. Clone the repository
2. Install the dependencies with uv
```
uv sync --locked --all-extras --dev
```
3. Download  the following assets and put them in a `examples` folder in your current directory.

[classic-car.heic](https://github.com/e-vdb/heic-to-jpg-converter/releases/download/v0.1.0/classic-car.heic)

[greyhounds-looking-for-a-table.heic](https://github.com/e-vdb/heic-to-jpg-converter/releases/download/v0.1.0/greyhounds-looking-for-a-table.heic)

[sewing-threads.heic](https://github.com/e-vdb/heic-to-jpg-converter/releases/download/v0.1.0/sewing-threads.heic)

[soundboard.heic](https://github.com/e-vdb/heic-to-jpg-converter/releases/download/v0.1.0/soundboard.heic)
5. Run the demo script
```
uv run main.py
```

The script will convert all the images in the `examples` folder to JPEG and save them in a child folder starting with a unique id.
