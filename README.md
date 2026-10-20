# runway-fod-detection

FIT1061 project exploring computer vision for runway foreign object debris detection.

## Get started

The starter notebook is at `notebooks/fod_detection.ipynb`. Open it from this repository's root folder so its `scripts.selective_images` import resolves. Install the current helper's dependency with `pip install -r requirements.txt`.

For Google Colab, open the notebook from GitHub, then run this setup cell before its import cell (replace the URL if you use a fork):

```python
!git clone https://github.com/dihen-e/runway-fod-detection.git
%cd runway-fod-detection
!pip install -r requirements.txt
```

The notebook currently contains a starter import, not a trained detection model. Image datasets are stored outside this Git repository and are not included here.
