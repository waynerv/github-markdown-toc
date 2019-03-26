from gfm_toc.md_toc import generate_toc


def test_generate_toc():
    with open('test_file.md', 'r') as f:
        # 测试起始与结束标题级别的边界条件
        toc_result01 = generate_toc(f, 4, 2)
        assert toc_result01 is None
        # 测试能否返回预期行数的结果
        toc_result02 = generate_toc(f)
        assert toc_result02.count('\n') == 25
        f.seek(0)
        # 测试能否跳过代码块内标题
        toc_result03 = generate_toc(f)
        assert 'This is an <h6> tag' not in toc_result03 and ('Emphasis' in toc_result03)
        f.seek(0)
        # 测试能否删除标题文本中的HTML标签
        toc_result04 = generate_toc(f)
        assert '<span>Emoji<span>' not in toc_result04
        f.seek(0)
        # 测试标题锚点能否将标题转换为小写，并删除空格与多余符号
        toc_result05 = generate_toc(f)
        assert 'username-mentions' in toc_result05
        f.seek(0)
        # 测试标题锚点能否处理重复标题
        toc_result06 = generate_toc(f)
        assert 'blockquotes-1' in toc_result06 and 'blockquotes-2' in toc_result06
        f.seek(0)
        # 测试输出的目录条目缩进是否与标题级别匹配
        toc_result07 = generate_toc(f)
        assert toc_result07.find('  ') < toc_result07.find('    ')
