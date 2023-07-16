from transformers import *
import re
import numpy as np

tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased")

def bert_tokenizer(sent, MAX_LEN) :
    encoded_dict = tokenizer.encode_plus(
        text = sent1,
        text_pair = sent2,
        add_special_tokens = True,
        max_length = MAX_LEN,
        pad_to_max_length = True,
        return_attention_mask = True
        truncation = True
    )

    input_id = encoded_dict['input_ids']
    attention_mask = encoded_dict['attention_mask']

    token_type_id = encoded_dict['token_type_ids']
    return input_id, attention_mask, token_type_id


# Special Tokens
print(tokenizer.all_special_tokens, "\n", tokenizer.all_special_ids)

# Test Tokenizers
kor_encode = tokenizer.encode("안녕하세요, 반갑습니다")
eng_encode = tokenizer.encode("Hello world ")
kor_decode = tokenizer.decode(kor_encode)
eng_decode = tokenizer.decode(eng_encode)

print(kor_decode)
print(eng_encode)

print(kor_decode)
print(eng_decode)

input_ids = []
attention_masks = []
token_type_ids = []
train_data_labels = []


def clean_text(sent):
    sent_clean = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]", " ", sent)
    return sent_clean

for train_set, train_label in zip(train_data["document"], train_data["label"]) :
    try :
        input_id, attention_mask, token_type_id = bert_tokenizer(clean_text(train_set), MAX_LEN)
        input_ids.append(input_id)
        attention_masks.append(attention_mask)
        token_type_ids.append(token_type_id)
        train_data_labels.append(train_label) 
    except Exception as e :
        print(e)
        print(train_sent)
        pass

train_movie_input_ids = np.array(input_ids, dtype=int)
train_movie_attention_masks = np.array(attention_masks, dtype=int)
train_movie_type_ids = np.array(token_type_ids, dtype=int)
train_movie_inputs = (train_movie_input_ids, train_movie_attention_masks, train_movie_type_ids)

train_data_labels = np.asarray(train_data_labels, dtype=np.int32)

print("# sents: {}, # labels: {}".format(len(train_movie_input_ids), len(train_data_labels)))

# Max length 39
input_id = train_movie_input_ids[1]
attention_mask = train_movie_attention_masks[1]
token_type_id = train_movie_type_ids[1]

print(input_id)
print(attention_mask)
print(token_type_id)
print(tokenizer.decode(input_id))