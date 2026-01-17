#  Narrative Consistency Detection System

## Problem Overview

This project addresses **Track A** by determining whether a given **narrative caption (backstory)** is **consistent or contradictory** with a corresponding **story excerpt**.

The task is modeled as a **binary classification problem**:
- **1 → Consistent**
- **0 → Contradict**

The focus of this solution is on **interpretable reasoning**, **modular design**, and **robust execution** without reliance on black-box models.

---

## Solution Summary

The system is implemented as a **multi-stage reasoning pipeline**, where each stage performs a distinct role:

1. **Data Ingestion**
2. **Signal Retrieval**
3. **Explainable Scoring**
4. **End-to-End Prediction**

This structure demonstrates **agentic behavior**, where the system retrieves evidence, reasons over it, and makes autonomous decisions.

---

## Project Structure


---

## Pipeline Description

### 1. Ingestion (`ingest.py`)
- Loads training data
- Converts labels into numeric form
- Displays class distribution
- Prepares a Pathway-compatible table schema

**Note:**  
Pathway Engine does not currently support Windows environments.  
To handle this, Pathway is **mocked locally** while preserving the same schema and orchestration logic.  
The pipeline runs unmodified in Linux/Docker environments with Pathway Engine.

---

### 2. Retrieval (`retrieve.py`)
This module extracts **interpretable signals** from the caption and content, including:
- Lexical overlap ratio (Jaccard similarity)
- Negation asymmetry detection
- Caption absence flag

These signals act as evidence for consistency or contradiction.

---

### 3. Scoring (`score.py`)
Signals are combined using **explainable rule-based logic**:
- High overlap increases consistency
- Negation mismatch penalizes the score
- Missing captions default to consistency

This avoids opaque models and ensures transparency.

---

### 4. Prediction (`predict.py`)
The final pipeline:
- Iterates over test samples
- Applies retrieval and scoring
- Produces predictions in the required format

Output example:


---

## How to Run the Project

Run each stage sequentially:

```bash
python ingest.py
python retrieve.py
python score.py
python predict.py
