import argparse
import re
import sys


def generate_toc(file_object, start_level=1, end_level=6):
    if start_level > end_level:
        return
    output_md = ""
    anchor_tracker = {}
    block_flag = False
    # Compile regular expression objects
    # 编译需要重复使用的正则表达式对象
    regex_title = re.compile(r'^(#+) (.*)$')
    regex_tag = re.compile(r'<.*?>')
    regex_char = re.compile(r'[^_a-z0-9\u4e00-\u9fa5- ]')
    regex_space = re.compile(r' ')
    regex_block = re.compile(r'^\s*```')

    for process_line in file_object:
        # Check if the text is inside the code block
        # 检查文本是否在代码块内
        if regex_block.match(process_line):
            if block_flag:
                block_flag = False
            else:
                block_flag = True
        # If the text is in the code block, skip the title matching and subsequent processing of the line text.
        # 若文本在代码块内，则跳过该行文本的标题匹配与后续处理
        if block_flag:
            continue
        else:
            # Perform a regular match on current line, returning a match object
            # 对该行文本执行标题的正则匹配，返回一个match object
            match = regex_title.search(process_line)

            if match:
                heading_level = len(match.group(1))

                # Skip headers that are not within the specified heading level
                # 跳过不在指定标题级别范围内的标题
                if heading_level < start_level or heading_level > end_level:
                    continue

                # Delete the HTML tag in the text
                # 删除标题文本中的HTML tag
                heading_title = regex_tag.sub('', match.group(2))
                # Generate heading anchor, convert text to lowercase, and remove spaces or extra symbols from text
                # 生成锚点，将标题文本转换为小写，并删除标题文本中的空格与多余符号
                heading_anchor = regex_char.sub('', (heading_title.lower()))
                heading_anchor = regex_space.sub('-', heading_anchor)

                # Refer to the GFM specification to process the same heading anchor
                # 参照GFM规范，对转换后文本相同的标题锚点进行处理
                if heading_anchor not in anchor_tracker:
                    anchor_tracker[heading_anchor] = 0
                else:
                    anchor_tracker[heading_anchor] += 1
                    heading_anchor = heading_anchor + '-' + str(anchor_tracker[heading_anchor])

                # Indented space multiple of the output result
                # 输出结果的缩进空格倍数
                indents = heading_level - start_level

                # Output the formatted TOC entry, such as: - [Use FlaskForm-Migrate](#use-flaskform-migrate)
                # 输出格式化后的目录条目，如：- [Use FlaskForm-Migrate](#use-flaskform-migrate)
                output_md += " " * (indents * 2) + "- [" + heading_title + "](#" + heading_anchor + ")\n"

    return output_md


def handler(filenames, start_level, end_level, write_flag=True, title_flag=False):
    for filename in filenames:
        with open(filename, 'r+') as f:
            toc = generate_toc(f, start_level, end_level)
            if title_flag:
                toc = '## Table of contents\n\n' + toc
            if write_flag:
                f.seek(0)
                data = f.read()
                f.seek(0)
                f.write(toc + '\n' + data)
            else:
                print('Generate from file: {}\n'.format(filename))
                print(toc)
    print('Table of contents generated.')


def main():
    # Add command line arguments
    # 配置命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', metavar='file', nargs='+', help='file or files to generate TOC')
    parser.add_argument('-s', '--start', type=int, choices=[1, 2, 3, 4, 5, 6], default=1,
                        help='choose the start level of TOC, default value is 1')
    parser.add_argument('-e', '--end', type=int, choices=[1, 2, 3, 4, 5, 6], default=6,
                        help='choose the end level of TOC, default value is 6')
    parser.add_argument('-o', '--output', action='store_true', help='print toc to stdout instead of writing to file')
    parser.add_argument('-t', '--title', action='store_true', help='add a level 2 title to the generated TOC')
    args = parser.parse_args()

    # Get command line arguments
    # 获取命令行参数
    start_level = args.start
    end_level = args.end
    if start_level > end_level:
        sys.exit('command option is illegal: start level must less than or equal to end level.')
    filenames = args.filenames

    if args.output:
        write_flag = False
    else:
        write_flag = True
    title_flag = args.title
    handler(filenames, start_level, end_level, write_flag, title_flag)


if __name__ == '__main__':
    main()
