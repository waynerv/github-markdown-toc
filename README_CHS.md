# gfm-toc

[中文文档](<https://github.com/waynerv/github-markdown-toc/blob/master/README_CHS.md>) | [Readme](<https://github.com/waynerv/github-markdown-toc/blob/master/README.md>)

## 目录

  - [简介](#简介)
  - [安装](#安装)
  - [使用](#使用)
    - [单个文件](#单个文件)
    - [多个文件](#多个文件)
    - [配置](#配置)
      - [自定义目录的标题级别](#自定义目录的标题级别)
      - [将结果写入到文件或打印到标准输出](#将结果写入到文件或打印到标准输出)
      - [为生成的目录添加标题](#为生成的目录添加标题)
  - [环境依赖](#环境依赖)

## 简介

简单且可自定义的方式为 Github Markdown 文件自动生成目录。

- 遵照 Github Favored Markdown 格式自动生成目录
- 单个.py文件即可运行，无其他依赖
- 支持中文与英文语言的文本内容
- 支持自定义生成目录的标题级别
- 支持自动将结果写入文件，也可打印结果到标准输出自行处理
- 支持同时为多个文件生成目录
- 支持重复标题、过滤代码块中的标题

如果你不想下载任何文件或者阅读下面的命令说明，可以尝试一下我的在线生成工具。

## 安装

**Pypi**

```bash
$ pip3 install gfm-toc --upgrade
```

**手动安装**

```bash
$ git clone https://github.com/waynerv/github-markdown-toc
$ cd github-markdown-toc
$ python3 setup.py install
```

也可直接下载仓库目录中的`gfm_toc/md_toc.py`文件并像下面这样手动运行脚本：

```bash
$ python3 md-toc.py [-h] [-s {1,2,3,4,5,6}] [-e {1,2,3,4,5,6}] [-o] file [file ...]
```

## 使用

命令格式如下：

```bash
$ gfm-toc [-h] [-s {1,2,3,4,5,6}] [-e {1,2,3,4,5,6}] [-o] file [file ...]
```

以如下方式运行命令可获取命令选项的帮助信息（可将`-h`替换成`--help`）：

```bash
$ gfm-toc -h
```

注意：使用前请确保你的设备已经成功安装了 Python3。

### 单个文件

为单个 markdown 文件自动生成目录并打印到标准输出，目录中仅包含1-3级标题：

```bash
$ gfm-toc -s 1 -e 3 -o README.md
Generate from file: README.md

- [目录](#目录)
- [md-toc](#md-toc)
- [安装](#安装)
- [使用](#使用)
  - [单个文件](#单个文件)
  - [多个文件](#多个文件)
  - [配置](#配置)
    - [自定义目录的标题级别](#自定义目录的标题级别)
    - [将结果写入到文件或打印到标准输出](#将结果写入到文件或打印到标准输出)
- [环境依赖](#环境依赖)

Table of contents generated.
```

然后将命令提示语句之间的结果从终端复制粘贴到原来的 README.md 文件中。

### 多个文件

使用默认配置为多个md文件自动生成目录并分别写入到文件中：

```bash
$ gfm-toc file01.md file02.md file03.md
Table of contents generated.
```

原文件示例：

- [File_without_TOC.md](https://github.com/waynerv/github-markdown-toc/blob/master/examples/File_without_TOC.md)

自动生成目录并写入到文件后：

- [File_with_TOC.md](https://github.com/waynerv/github-markdown-toc/blob/master/examples/File_with_TOC.md)

### 配置

#### 自定义目录的标题级别

使用命令行选项 `-s` 或 `--start` 并添加参数即可设置生成目录的起始标题级别，参数默认值为1。

使用命令行选项 `-e` 或 `--end` 并添加参数即可设置生成目录的结束标题级别，参数默认值为6。

标题级别参数必须是1到6之间的整数，且起始标题级别不能大于结束标题级别。

```bash
-s {1,2,3,4,5,6}, --start {1,2,3,4,5,6}  choose the start level of TOC, default value is 1
-e {1,2,3,4,5,6}, --end {1,2,3,4,5,6}  choose the end level of TOC, default value is 6
```

生成1-6级标题的目录（默认选项）：

```bash
$ gfm-toc test/Mastering_Markdown.md -o
Generate from file: test/Mastering_Markdown.md

- [Mastering Markdown](#mastering-markdown)
  - [What is Markdown?](#what-is-markdown)
  - [Examples](#examples)
  - [Syntax guide](#syntax-guide)
    - [Headers](#headers)
    - [Emphasis](#emphasis)
    - [Lists](#lists)
      - [Unordered](#unordered)
      - [Ordered](#ordered)
    - [Images](#images)
    - [Links](#links)
    - [Blockquotes](#blockquotes)
    - [Inline code](#inline-code)

Table of contents generated.
```

只生成2-3级标题的目录：

```bash
$ gfm-toc examples/Mastering_Markdown.md -o -s 2 -e 3
Generate from file: examples/Mastering_Markdown.md

- [What is Markdown?](#what-is-markdown)
- [Examples](#examples)
- [Syntax guide](#syntax-guide)
  - [Headers](#headers)
  - [Emphasis](#emphasis)
  - [Lists](#lists)
  - [Images](#images)
  - [Links](#links)
  - [Blockquotes](#blockquotes)
  - [Inline code](#inline-code)

Table of contents generated.
```

#### 将结果写入到文件或打印到标准输出

默认情况下程序会将生成的目录自动写入到原文件的开头。

在使用时添加选项`-o`或`--output` 即可将结果直接打印到标准输出供复制或进行其他处理。

```bash
-o, --output          print toc to stdout instead of writing to file
```

在命令行中使用 `>` 重定向数据流即可将生成的目录输出到单独的文件中：

```bash
$ gfm-toc -o README.md > table_of_content.md
```

#### 为生成的目录添加标题

这个选项并不会很常用，因为很多情况下，人们按照不同的规范或自己的习惯编写Markdown文档。但如果你需要的话，可以在执行命令时添加 `-t` 或 `--title` 选项，这会为生成的整个目录添加一个名为 `Table of contens` 的二级标题，如下：

```bash
$ gfm-toc examples/Mastering_Markdown.md -o -s 2 -e 3 -t
Generate from file: examples/Mastering_Markdown.md

## Table of contents

- [What is Markdown?](#what-is-markdown)
- [Examples](#examples)
- [Syntax guide](#syntax-guide)
  - [Headers](#headers)
  - [Emphasis](#emphasis)
  - [Lists](#lists)
  - [Images](#images)
  - [Links](#links)
  - [Blockquotes](#blockquotes)
  - [Inline code](#inline-code)

Table of contents generated.
```

## 环境依赖

- Python3

在 Ubuntu 18.04 python 3.6 环境使用 bash 终端进行过测试。
