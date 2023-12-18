from langchain.text_splitter import CharacterTextSplitter

# This is a long document we can split up.
with open('state_of_the_union_chinese2.txt', encoding="utf-8") as f:
    state_of_the_union = f.read()

# 文本切割，最重要的参数：
# chunk_size 块大小 是块可以包含的最大字符数。
# chunk_overlap 块重叠 是块重叠两个相邻块之间应重叠的字符数。
    
# 这里需要了解的重要参数是chunkSize 和chunkOverlap。
#  chunkSize 控制最终文档的最大大小（以字符数计）。
#  chunkOverlap 指定块之间应该有多少重叠。这通常有助于确保文本不会被奇怪地分割。
# 在下面的示例中，我们将这些值设置得很小（出于说明目的），但实际上它们分别默认为 1000 和 200。
    
# 参考文档：https://js.langchain.com/docs/modules/data_connection/document_transformers/
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False,
)

texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])
print(len(texts[0].page_content))
print(texts[1])
print(len(texts[1].page_content))

l = len("二、经典作品是这样一些书，它们对读过并喜爱它们的人构成一种宝贵的经验；但是对那些保留这个机会，等到享受它们的最佳状态来临时才阅读它们的人，它们也仍然是一种丰富的经验。\n\n\u3000\u3000因为实际情况是，我们年轻时所读的东西，往往价值不大，这又是因为我们没耐性、精神不能集中、缺乏阅读技能，或因为我们缺乏人生经验。这种青少年的阅读可能（也许同时）具有形成性格的作用，理由是它赋予我们未来的经验一种形式或形状，为这些经验提供模式，提供处理这些经验的手段，比较的措辞，把这些经验加以归类的方法，价值的衡量标准，美的范例： 这一切都继续在我们身上起作用，哪怕 我们已差不多忘记或完全忘记我们年轻时所读的那本书。当我们在成熟时期重读这本书，我们就会重新发现那些现已构成我们内部机制的一部分的恒定事物，尽管我们已回忆不起它们从哪里来。这种作品有一个特殊效力，就是它本身可能会被忘记，却把种籽留在我们身上。我们现在可以给出这样的定义：\n\n\u3000\u3000三、经典作品是一些产生某种特殊影响的书，它们要么自己以遗忘的方式给我们的想像力打下印记，要么乔装成个人或集体的无意识隐藏在深层记忆中。\n\n\u3000\u3000基于这个理由，一个人的成年生活应有一段时间用于重新发现我们青少年时代读过的最重要作品。即使这些书依然如故（其实它们也随着历史角度的转换而改变），我们肯定已经改变了，因此后来这次接触也就是全新的。\n\u3000\u3000所以，我们用动词“读”或动词“重读”也就不真的那么重要。事实上我们可以说：\n\n\u3000\u3000四、一部经典作品是一本每次重读都好像初读那样带来发现的书。\n\n\u3000\u3000五、一部经典作品是一本即使我们初读也好像是在重温我们以前读过的东西的书。\n\n\u3000\u3000上述第四个定义可视为如下定义的必然结果：\n\n\u3000\u3000六、一部经典作品是一本从不会耗尽它要向读者说的一切东西的书。\n\n\u3000\u3000而第五个定义则隐含如下更复杂的方程式：\n\n\u3000\u3000七、经典作品是这样一些书，它们带着以前的解释的特殊气氛走向我们，背后拖着它们经过文化或多种文化（或只是多种语言和风俗习惯）时留下的足迹。")
print(l)