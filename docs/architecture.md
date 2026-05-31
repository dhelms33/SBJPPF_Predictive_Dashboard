```mermaid 

graph TD 
    A[Raw CSV Export] --> B(ParserFactory)
    B -->| If Facebook| C[Facebook Parser]
    B -->| If Instagram| D[Instagram Parser]
    C --> E[Data Pipeline / Feature Extraction]
    D --> E [Predictive Engine / Strategy Pattern]