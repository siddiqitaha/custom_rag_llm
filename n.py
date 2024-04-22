import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.rouge_score import rouge_scorer

def calculate_precision_recall_f1(y_true, y_pred):
    precision = precision_score(y_true, y_pred, average='binary')
    recall = recall_score(y_true, y_pred, average='binary')
    f1 = f1_score(y_true, y_pred, average='binary')
    return precision, recall, f1

def calculate_bleu(reference, candidate):
    # Assuming reference and candidate are lists of words
    return sentence_bleu([reference], candidate)

def calculate_rouge(reference, candidate):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(' '.join(reference), ' '.join(candidate))
    return scores

# Example: Load your data here
ground_truth_answers = [
    "1495",
    "William Elphinstone, Bishop of Aberdeen and Chancellor of Scotland",
    "King's College and Marischal College",
    "Initium sapientiae timor domini; The fear of the Lord is the beginning of wisdom",
    "The Crown Tower is an iconic symbol of the university, representing its history and academic excellence",
    "The university contributed to intellectual development, innovation, and the promotion of enlightenment thought",
    "It combines elements from the arms of the founding colleges, reflecting their merger and the university's heritage",
    "It led to a shift from Catholic to Protestant teaching and changes in governance structures",
    "Marischal College played a critical role in promoting enlightenment thought, particularly in philosophy, science, and medicine",
    "It evolved from medieval buildings to modern facilities, expanding significantly in the 20th century",
    "The controversy involves proposed changes to the program due to financial constraints and declining enrollment, with backlash from the academic community",
    "King's College had a religious and educational focus since its Catholic founding, while Marischal College was a Protestant alternative",
    "The university has expanded its curriculum to include a wide range of disciplines beyond its historical focus",
    "This requires analysis of budget, endowment, income from research grants, and expenditures provided in the Wikipedia page or official reports",
    "It underscores the university's significant contributions to global knowledge and research excellence",
    "It involves issues of transparency, accountability, and governance in the use of university funds",
    "The motto suggests a foundational respect for knowledge and wisdom, guiding the university's ethical approach to education and research",
    "Initiatives might include expanding global education programs, interdisciplinary research, and focusing on sustainability",
    "The university should employ strategies to adapt to broader educational demands while emphasizing the importance of language studies",
    "The program would draw on the university's strengths in history, divinity, medicine, and the Scottish Enlightenment"
]  # A list of correct answers
predicted_answers = [...]     # A list of answers generated by your system

# Convert answers to a binary form for precision, recall, F1 calculations
binary_ground_truth = [1] * len(ground_truth_answers)  # All correct answers as '1'
binary_predicted = [1 if pred in ground_truth_answers else 0 for pred in predicted_answers]

# Calculate precision, recall, and F1 score
precision, recall, f1 = calculate_precision_recall_f1(binary_ground_truth, binary_predicted)
print(f"Precision: {precision}, Recall: {recall}, F1 Score: {f1}")

# Calculate BLEU and ROUGE for linguistic quality
bleu_scores = [calculate_bleu([gt.split()], pred.split()) for gt, pred in zip(ground_truth_answers, predicted_answers)]
rouge_scores = [calculate_rouge(gt.split(), pred.split()) for gt, pred in zip(ground_truth_answers, predicted_answers)]

average_bleu = np.mean(bleu_scores)
average_rouge1 = np.mean([score['rouge1'].fmeasure for score in rouge_scores])
average_rougeL = np.mean([score['rougeL'].fmeasure for score in rouge_scores])

print(f"Average BLEU Score: {average_bleu}")
print(f"Average ROUGE-1 Fmeasure: {average_rouge1}, Average ROUGE-L Fmeasure: {average_rougeL}")
