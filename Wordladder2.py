from collections import defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        graph = defaultdict(list)
        found = False
        forward, backward = {beginWord}, {endWord}
        direction = True  

        while forward and backward and not found:
           
            if len(forward) > len(backward):
                forward, backward = backward, forward
                direction = not direction

            wordSet -= forward  
            next_level = set()

            for word in forward:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            next_level.add(new_word)
                            if direction:
                                graph[word].append(new_word)
                            else:
                                graph[new_word].append(word)
                            if new_word in backward:
                                found = True
            forward = next_level

        res = []

        def dfs(path, word):
            if word == endWord:
                res.append(path[:])
                return
            for nxt in graph[word]:
                path.append(nxt)
                dfs(path, nxt)
                path.pop()

        if found:
            dfs([beginWord], beginWord)
        return res
