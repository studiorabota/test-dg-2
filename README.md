# test-dg

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/studiorabota/test-dg/blob/main/notebooks/lfs_demo.ipynb)

Small test repo: a Jupyter notebook that opens in Google Colab and loads a ~6 MB data file stored with **Git LFS**.

```
.
├── .gitattributes            # *.npy, *.nc, *.parquet … → Git LFS
├── data/
│   └── wind_speed_field.npy  # synthetic (24 h × 256 × 256) wind field, stored in LFS
└── notebooks/
    └── lfs_demo.ipynb        # clones the repo, pulls LFS files, plots the data
```

## Update the repo (command line, so LFS is used)

Files uploaded through the GitHub website skip hidden files like `.gitattributes`, so the data ends up in plain git instead of LFS. Push from the command line instead:

```bash
git clone https://github.com/studiorabota/test-dg.git
cd test-dg
git lfs install --local

# copy the contents of this zip into the folder (including .gitattributes), then:
git rm --cached -q lfs_demo.ipynb data/wind_speed_field.npy publish.sh   # remove the stray root copy + re-add data via LFS
rm -f lfs_demo.ipynb publish.sh
git add .gitattributes
git add .
git lfs ls-files        # should list data/wind_speed_field.npy
git commit -m "Fix Colab link, store data in Git LFS"
git push
```

## Test

1. On GitHub, `data/wind_speed_field.npy` should show **"Stored with Git LFS"**.
2. Click **Open in Colab** and choose **Runtime → Run all**.
3. The notebook checks that it got the real file (not an LFS pointer) and plots it.

## How it works / gotchas

- **The Colab button only loads the `.ipynb`**, not the repo. That's why the notebook clones the repo and runs `git lfs pull` itself.
- **Private repos:** Colab will ask to authorize GitHub when you open the notebook. Cloning *inside* the notebook needs a token: add a fine-grained token with read access as a Colab secret named `GH_TOKEN`.
- **Bandwidth:** every new Colab session downloads the LFS files again, which counts against your GitHub LFS bandwidth quota.
