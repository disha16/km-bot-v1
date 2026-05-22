# KM Bot v1

A lightweight knowledge management bot prototype for answering questions from approved source material. The first version is designed to keep the knowledge loop simple: collect a small set of trusted files, retrieve relevant excerpts, and use Manus for reasoning, synthesis, and cited answers.

## Initial Goal

The first milestone is a working question-answer loop over a small corpus of internal documents. The bot should answer from approved knowledge sources, cite where each material claim came from, and clearly say when the current corpus does not contain enough information.

## Repository Structure

```text
km-bot-v1/
  docs/
    product_brief.md
    prompt_contract.md
  knowledge/
    raw/
    processed/
  src/
    ingest/
    retrieval/
    bot/
  config/
    sources.example.json
  scripts/
```

## Suggested First Test

Add two or three source documents to `knowledge/raw/`, then test five questions: two factual questions, one synthesis question, one out-of-scope question, and one request for recommended next actions.

## Operating Principle

If an answer cannot be grounded in the approved corpus, the bot should say what is missing rather than guess.
