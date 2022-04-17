from typing import List, Dict

positives: List[int] = [0, 1, 2, 3, 4, 5]

users: Dict[str, int] = {
    'argentina': 4,
    'peru': 13,
    'mexico': 20
}

Countries = List[Dict[str, str]]

countries: Countries = [
    {
        'name': 'Argentina',
        'people': '450000'
    },
    {
        'name': 'Peru',
        'people': '650000'
    },
    {
        'name': 'Mexico',
        'people': '730000'
    }
]


def is_palindrome(word: str) -> bool:
    word = word.replace(' ', '').lower()
    return word == word[::-1]

def run():
    response = is_palindrome('101')
    print(response)

if __name__ == '__main__':
    run()