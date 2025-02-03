# CTF Writeup Analysis with NLP  

![License](https://img.shields.io/badge/license-MIT-blue.svg)  

## Overview  

This repository contains scripts and prompts for analyzing **Capture The Flag (CTF) writeups** using **Natural Language Processing (NLP)** techniques.  
The goal is to categorize **attacker behaviors, strategies, and techniques** extracted from CTF reports and create a structured **taxonomy** to classify and understand different attack methods.  

By leveraging **GPT models**, the system processes and organizes data into a structured format, making it easier to analyze recurring **tactics, techniques, and procedures (TTPs)** used in CTF challenges.  

## Features  

- **Automatic extraction** of attacker strategies from CTF writeups  
- **NLP-based classification** of attack techniques  
- **Taxonomy generation** for systematic attack categorization  
- **GPT-assisted processing** to structure and normalize CTF reports  
- **JSON output format** for further analysis and visualization  

## Background  

This project is based on a **Master’s Thesis at Politecnico di Torino**:  

> *Tassonomia dei comportamenti degli attaccanti nelle sfide di Capture The Flag (CTF): un approccio di categorizzazione attraverso l'analisi dei writeups*  
> *Francesco Lonardo, Academic Year 2022/2023*  

📄 **[Download the full thesis (PDF) - ITA](./s291039_francescolonardo_tesi.pdf)**  
📄 **[Download the thesis summary (PDF) - ITA](./s291039_francescolonardo_riassunto.pdf)**  

The research focuses on **analyzing attacker behaviors in CTF competitions** using AI-driven NLP models. Writeups from various sources were collected and processed using GPT-based techniques, with the ultimate goal of developing a **taxonomy** to classify and understand common attack patterns.  

## Methodology  

The methodology for analyzing CTF writeups and generating a structured taxonomy involves several key steps:  

### 1️. Data Collection  

A diverse set of **CTF writeups** was collected from public sources, primarily from **GitHub repositories** and cybersecurity blogs. The selection criteria included:  
- **Variety of attack techniques** to ensure a comprehensive taxonomy.  
- **Different CTF formats** (Jeopardy-style, Attack-Defense) to cover diverse attacker behaviors.  
- **Well-documented solutions** with detailed explanations of exploitation techniques.  

Writeups were retrieved using **GitHub APIs** and manually validated to ensure relevance.  

### 2️. Data Preprocessing and Normalization  

To process unstructured writeups efficiently, the data was **preprocessed** using Natural Language Processing (NLP) techniques:  
- **Text Cleaning:** Removing unnecessary metadata, formatting issues, and noise.  
- **Segmentation:** Splitting writeups into logical steps representing the attack process.  
- **Normalization:** Standardizing terms and extracting key attack behaviors.  

Each writeup was structured into a **JSON format**, breaking down attacks into individual **steps** and **sub-steps** for further analysis.  

### 3️. NLP-Based Classification  

The structured writeups were processed using **GPT models** to:  
- Identify **recurrent attack techniques** and categorize them accordingly.  
- Label each attack step with corresponding **MITRE ATT&CK tactics and techniques**.  
- Generate **summaries** to enhance readability and automate classification.  

### 4. Taxonomy Development  

A **hierarchical taxonomy** was developed to systematically classify attack behaviors. The taxonomy was created through:  
1. **Step extraction** – Identifying fundamental actions within each writeup.  
2. **Grouping similar techniques** – Categorizing attack patterns into broader behaviors.  
3. **Mapping to existing frameworks** – Aligning with MITRE ATT&CK, OWASP, and other cybersecurity models.  
4. **Iterative refinement** – Evaluating classification accuracy and improving taxonomy depth.  

### 5. Data Labeling and Validation  

The taxonomy was **iteratively refined** by:  
- Manually verifying NLP-generated labels.  
- Cross-referencing with established security frameworks.  
- Testing against new writeups to evaluate classification consistency.  

The final dataset provides a structured **collection of CTF attack techniques**, helping cybersecurity professionals **understand, categorize, and analyze** attacker behaviors more effectively.

## Future Work

This methodology can be extended to analyze **real-world security incidents**, providing insights beyond CTF challenges.  
Possible improvements include:
- **Automating extraction** from CTF platforms for continuous learning.  
- **Refining GPT prompts** to enhance classification accuracy.  
- **Applying the taxonomy to penetration testing reports** to identify common attacker patterns.  
- **Comparing results with real-world security incidents** to bridge the gap between CTF and practical cybersecurity threats.  
