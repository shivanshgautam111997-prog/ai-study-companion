class MockSearchTool:
    def search(self, query, top_k=2):
        safe = query.replace(" ", "_")
        return [
            {"title": f"{query} Intro", "url": f"https://example.com/{safe}"},
            {"title": f"{query} Examples", "url": f"https://example.com/{safe}/examples"}
        ][:top_k]
