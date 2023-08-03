from modelscope.pipelines import pipeline
from modelscope.models import Model
from modelscope.outputs import OutputKeys
from PIL import Image
import os

input = "https://vigen-video.oss-cn-shanghai.aliyuncs.com/VideoEnhancement/Dataset/ClassicalSRDataset/inputs/OST_009.png"

"""
本 demo 需要多CPU、大内存、大显存才能运行

官方的 demo 没有加 revision='v1.0.0' 无法下载模型，导致跑不通
如果要跑通，一定要加 revision 参数

就算加了也跑不通，因为官方免费版内存只有 16G，不够。
"""

model = Model.from_pretrained('xhlin129/cv_stablesr_image-super-resolution', revision='v1.0.0', steps=50)
inference = pipeline('stablesr-task', model=model)
output = inference(input, tile_overlap=16)
Image.fromarray(output[OutputKeys.OUTPUT_IMG]).save('result.png')
print(f'Output written to {os.path.abspath("result.png")}')