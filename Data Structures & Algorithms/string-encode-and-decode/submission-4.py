class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "Null"
        return "&&".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "Null":
            return []

        return s.split("&&")