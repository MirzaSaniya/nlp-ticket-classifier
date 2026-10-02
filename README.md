# NLP Support Ticket Classifier

A practical text-classification pipeline that automatically routes support requests into categories such as billing, access, bug reports, and feature requests.

## Business use case

Support queues often receive large volumes of unstructured text. Automated routing can reduce manual triage and help downstream teams prioritize the right category quickly.

## Pipeline

```text
Ticket text
   |
   v
Text normalization
   |
   v
TF-IDF vectorization
   |
   v
Logistic Regression
   |
   v
Predicted category + confidence
```

## Evaluation

The demo trains on a tiny transparent dataset and reports accuracy plus predictions on held-out examples. The purpose is to demonstrate an end-to-end ML workflow, not to claim production performance from toy data.

## Run

```bash
python examples/demo.py
```

## Tests

```bash
pytest -q
```

## Production extensions

- larger labeled dataset
- class imbalance handling
- calibration and confidence thresholds
- human-in-the-loop review for low-confidence predictions
- monitoring for data drift

## CS221 connection

Inspired by supervised-learning and feature-based classification concepts commonly covered in CS221. The dataset, application framing, implementation, and documentation are independently developed.

## GitHub metadata

**Repository name:** `nlp-ticket-classifier`

**Description:** A lightweight NLP text classifier for routing support tickets using TF-IDF features and linear classification.

**Topics:** `natural-language-processing` `text-classification` `tfidf` `machine-learning` `scikit-learn` `python` `classification` `cs221`
