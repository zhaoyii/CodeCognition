from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download(model_id='xhlin129/cv_stablesr_image-super-resolution', revision='v1.0.0')