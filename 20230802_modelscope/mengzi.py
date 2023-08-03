from modelscope.pipelines import pipeline                  
from modelscope.utils.constant import Tasks
import gradio as gr                

fill_mask_zh = pipeline(Tasks.fill_mask, model='langboat/mengzi-bert-base')
result_zh = fill_mask_zh('生活的真谛是[MASK]。')

print(result_zh['text'])
