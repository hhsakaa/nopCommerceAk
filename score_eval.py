from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

reference = ["This is a nopCommerce deployment guide"]
candidate = "This guide explains nopCommerce deployment"

bleu = sentence_bleu([reference], candidate.split())
scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
rouge = scorer.score(reference[0], candidate)

print(f"BLEU: {bleu}\nROUGE: {rouge}")
