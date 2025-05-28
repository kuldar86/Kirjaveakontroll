import language_tool_python

tool = language_tool_python.LanguageTool('et')

def check_spelling(text):
    matches = tool.check(text)
    results = []
    for match in matches:
        results.append({
            "context": match.context,
            "message": match.message,
            "replacements": match.replacements
        })
    return results
