import os.path

import wordcloud
from pprint import pprint
import cv2


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["e", "o", "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    word_dict = {}
    punctuations_list = [i for i in punctuations]
    for punctuation in punctuations_list:
        file_contents.replace(punctuation, "", file_contents.count(punctuation))
    single_words = file_contents.split()
    for single_word in single_words:
        if single_word not in uninteresting_words:
            if single_word.__len__() > 1:
                if single_word not in word_dict:
                    word_dict[single_word] = 1
                else:
                    word_dict[single_word] = word_dict[single_word] + 1

    for file_content in file_contents:
        if file_content not in uninteresting_words:
            single_words = file_content.split()
            for single_word in single_words:
                if single_word not in punctuations:
                    if single_word.__len__() > 1:
                        if single_word not in word_dict:
                            word_dict[single_word] = 1
                        else:
                            word_dict[single_word] = word_dict[single_word] + 1
    # pprint(word_dict)
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dict)
    return cloud.to_array()
    
    
# Display your wordcloud image
file_contents = open("Input_text.txt", 'r', encoding='utf-8')
try:
    file_contents = file_contents.read()
except UnicodeDecodeError:
    print("Please keep only english text")
myimage = calculate_frequencies(file_contents)
img_name = "word_cloud_image.png"
cv2.imwrite(img_name, myimage)
if os.path.isfile(img_name) is  True:
    print("Image is generated with name: {}.".format(img_name))
