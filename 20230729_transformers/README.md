## 为什么要设置`os.environ["http_proxy"] = http_proxy`?

当你在 Python 中使用`os.environ["http_proxy"] = http_proxy`，你是在做以下几件事情：

1. **设置环境变量**：为当前的 Python 进程设置一个名为 `http_proxy` 的环境变量。
2. **控制网络请求**：指示 Python 和其他支持此设置的库使用指定的 HTTP 代理服务器进行网络通信。
3. **绕过网络限制**：允许程序在需要通过代理服务器访问外部网络的环境中正常工作。
4. **临时性的设置**：这种设置只影响当前进程。如果程序结束，此设置不会保存或影响其他进程。

简而言之，这个设置允许 Python 应用程序通过指定的 HTTP 代理进行网络请求。

从`Hugging Face`网站下载模型，实际上是从`AWS S3`下载模型。`AWS S3`是亚马逊的对象存储云服务，在中国大陆无法下载，需要通过代理下载模型。如果你在中国大陆，需要设置`os.environ["http_proxy"] = http_proxy`，以便通过代理下载模型。

## Hugging Face 模型文件的目录结构？
从 Hugging Face 网站下载的所有模型，位于`~\.cache\huggingface\hub`目录下。例如：
```
~/.cache/huggingface/hub
├── models--bert-base-chinese
├── models--bert-base-multilingual-cased
├── models--distilbert-base-uncased-finetuned-sst-2-english
├── models--finiteautomata--bertweet-base-sentiment-analysis
├── models--gpt2
├── models--suno--bark
├── models--uer--gpt2-chinese-cluecorpussmall
├── tmpr8jw870y
└── version.txt
```

以`models--distilbert-base-uncased-finetuned-sst-2-english`模型为例，其内部目录结构：
```
models--distilbert-base-uncased-finetuned-sst-2-english
├── .no_exist
|  └── 3d65bad49c7ba6f71920504507a8927f4b9db6c0
|     ├── added_tokens.json
|     ├── special_tokens_map.json
|     └── tokenizer.json
├── blobs
├── refs
|  └── main
└── snapshots
   └── 3d65bad49c7ba6f71920504507a8927f4b9db6c0
      ├── config.json
      ├── model.safetensors
      ├── tokenizer_config.json
      └── vocab.txt
```

- `config.json`是模型的配置文件。它存储了与特定模型架构相关的所有配置参数。例如，对于一个 BERT 模型，config.json 会包含模型大小、隐藏层的数量、隐藏单元的数量、注意力头的数量等参数。当你想重新加载一个模型时，这些配置参数是必要的，因为它们决定了模型架构的结构。
- `model.safetensors`是模型的二进制文件，通常非常大。最少都有几百兆，例如示例模型`model.safetensors`有 261MB。

参考。。。