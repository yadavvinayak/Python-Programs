# Repository Overview Flowchart

This diagram shows the repository's directory organization. It is not a call graph and does not imply that scripts execute one another.

```mermaid
flowchart TD
    ROOT["Python Programs repository"]
    ROOT --> CORE["Core examples"]
    ROOT --> CP["Competitive programming"]
    ROOT --> NEW["Topic-based examples"]
    ROOT --> TOP["Standalone practice files"]
    CORE --> P["Programs"]
    CORE --> O["OOP"]
    CORE --> N["NumPy"]
    CORE --> S["Scripts"]
    CP --> CC["CodeChef"]
    CP --> HE["HackerEarth"]
    CP --> SP["SPOJ"]
    NEW --> TOPICS["Topic folders"]
    TOPICS --> T_ArrayListPrograms["Lists and arrays"]
    TOPICS --> T_BasicPythonPrograms["Python basics"]
    TOPICS --> T_DateTimePrograms["Date and time"]
    TOPICS --> T_DictionaryPrograms["Dictionaries"]
    TOPICS --> T_FileHandlingPrograms["File handling"]
    TOPICS --> T_MatrixPrograms["Matrices"]
    TOPICS --> T_MorePythonPrograms["Math and other algorithms"]
    TOPICS --> T_PatternPrograms["Patterns"]
    TOPICS --> T_RegexPrograms["Regular expressions"]
    TOPICS --> T_SearchingSortingPrograms["Searching and sorting"]
    TOPICS --> T_StringPrograms["Strings"]
    TOPICS --> T_TuplePrograms["Tuples"]
```

## Inventory

- Python files: **486**
- Directories containing Python files: **31**
- Full file-by-file links: [Complete program index](program-index.md)
