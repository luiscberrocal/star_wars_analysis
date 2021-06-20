import re


def extract_paragraphs(raw_lines):
    paragraphs = dict()

    paragraph_num = 1
    paragraphs[paragraph_num] = dict()
    paragraphs[paragraph_num]['lines'] =list()

    for line in raw_lines:
        if line == '\n':
            paragraph_num += 1
            paragraphs[paragraph_num] = dict()
            paragraphs[paragraph_num]['lines'] =list()
        else:
            paragraphs[paragraph_num]['lines'].append(line.replace('\n', '').replace('\t', '').replace('�', 'E'))
    return paragraphs


def parse_paragraphs(paragraphs, **kwargs):
    actor_regexp = re.compile(r'(([A-Z\-0-9]+)\s?([A-Z0-9\-]+)?)')
    actor_lines = dict()
    #print(paragraphs[161])
    for p_num, content in paragraphs.items():
        #actor_lines[p_num]['actor'] = ''
        if len(content['lines']) >0:
            match = actor_regexp.match(content['lines'][0])
            if match and len(content['lines']) > 1:
                actor_lines[p_num]= dict()
                actor_lines[p_num]['actor'] = match.group(1)
                actor_lines[p_num]['lines'] = content['lines'].copy()
                actor_lines[p_num]['lines'].pop(0)
                #print(f'========= {p_num} {actor_lines[p_num]["actor"]} =====')
                #print(actor_lines[p_num]['lines'])
            else:
                pass
                #print(f'>>> {p_num}')
                #print(content['lines'])
                #print('>>>'*60)
        else:
            pass
            #print(f'>>>> Paragraph {p_num} is empty')
            #print(content['lines'])
    return actor_lines

def parse_paragraph_sep(paragraphs, **kwargs):
    character_regexp = re.compile(r'(?P<character>(?:(?:[A-Z\-0-9]{2,})(?:\s|\:)?)+)')
    character_lines = dict()
    for p_num, content in paragraphs.items():
        if ':' in content['lines'][0]:
            line_parts = content['lines'][0].split(':')
            match = character_regexp.match(line_parts[0])
            if match:
                character_lines[p_num] = dict()
                character_lines[p_num]['actor'] = match.group('character')
                content['lines'] = line_parts[1:]
                content['lines'][0] = content['lines'][0].strip()
                character_lines[p_num]['lines'] = content['lines'].copy()
                #character_lines[p_num]['lines'].pop(0)
    return character_lines

def build_dialogue_dict(character_lines):
    df_dict = dict()
    df_dict['Paragraph'] = list()
    df_dict['Character'] = list()
    df_dict['Dialogue'] = list()
    for p_num, content in character_lines.items():
        df_dict['Paragraph'].append(p_num)
        df_dict['Character'].append(content['actor'])
        df_dict['Dialogue'].append(' '.join(content['lines']))
    return df_dict
