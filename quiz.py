BLACK = "\033[90m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
WHITE = "\033[97m"

quiz_list = [
  {
    'subject': 'Engineering Math',
    'item_list': [
      {
        'question': 'The gradient of a straight line that has the equation y = 3x + 4 is...',
        'choice_dict': {
          'a': '3',
          'b': '4',
          'c': '1',
          'd': '2',
        },
        'answer': 'a',
      },
      {
        'question': 'The gradient of a straight line passing through the point 2x + y - 7 = 0 is...',
        'choice_dict': {
          'a': '2',
          'b': '7',
          'c': '3',
          'd': '-2',
        },
        'answer': 'd',
      },
      {
        'question': 'The gradient of a straight line passing through the point -3x + y + 5 = 0 is...',
        'choice_dict': {
          'a': '-3',
          'b': '3',
          'c': '5',
          'd': '1',
        },
        'answer': 'b',
      },
    ],
  },
  {
    'subject': 'Algorithms & Basic Programming',
    'item_list': [
      {
        'question': 'The logical steps to solve a programming problem are...',
        'choice_dict': {
          'a': 'Probability',
          'b': 'Algoritma',
          'c': 'Availability',
          'd': 'Program',
        },
        'answer': 'b',
      },
      {
        'question': 'The model of writing and designing algorithms using space symbols to represent program processes is called...',
        'choice_dict': {
          'a': 'Flowchart',
          'b': 'Laravel',
          'c': 'Building space algorithm',
          'd': 'Pseudocode',
        },
        'answer': 'a',
      },
      {
        'question': 'If p=5, q=10, then given the instruction p=q; q=p will result in: ...',
        'choice_dict': {
          'a': 'p=5, q=0',
          'b': 'p=5, q=10',
          'c': 'p=q',
          'd': 'p=10, q=10',
        },
        'answer': 'd',
      },
      {
        'question': 'The result of 4 + 3 % 5 is...',
        'choice_dict': {
          'a': '7',
          'b': '2',
          'c': '9',
          'd': '6',
        },
        'answer': 'a',
      },
    ],
  },
  {
    'subject': 'Introduction to Information Technology',
    'item_list': [
      {
        'question': 'The Linux distro that is a derivative of the Red Hat Linux distro is...',
        'choice_dict': {
          'a': 'Kali Linux',
          'b': 'Fedora',
          'c': 'Linux Mint',
          'd': 'Garuda Linux',
        },
        'answer': 'b',
      },
      {
        'question': 'The version name of the Android 9 OS is...',
        'choice_dict': {
          'a': 'KitKat',
          'b': 'Oreo',
          'c': 'Q',
          'd': 'Pie',
        },
        'answer': 'd',
      },
      {
        'question': 'Here are the different versions of Windows, except...',
        'choice_dict': {
          'a': 'Windows 7',
          'b': 'Windows Vista',
          'c': 'Windows 9',
          'd': 'Windows 10',
        },
        'answer': 'c',
      },
    ],
  },
]

def banner():
  print(f'''{BLUE}
    ______    ____  ____   __   ________         _______  ___  ___  
   /    {WHITE}"{BLUE} \  ({WHITE}"{BLUE}  _||_ {WHITE}"{BLUE} | |{WHITE}"{BLUE} \ ({WHITE}"      "{BLUE}\       |   __ {WHITE}"{BLUE}\|{WHITE}"{BLUE}  \/{WHITE}"{BLUE}  | 
  /{WHITE}/{BLUE} ____  \ |   (  ) {WHITE}:{BLUE} | |{WHITE}|{BLUE}  | \___/   {WHITE}:{BLUE})      ({WHITE}.{BLUE} |__) {WHITE}:{BLUE})\   \  /  
 /  /    )  )({WHITE}:{BLUE}  |  | {WHITE}.{BLUE} ) |{WHITE}:{BLUE}  |   /  ___/       |{WHITE}:{BLUE}  ____/  \\  \/   
({WHITE}:{BLUE} (____/ {WHITE}/{BLUE}/  \\ \__/ {WHITE}/{BLUE}/  |{WHITE}.{BLUE}  |  /{WHITE}/{BLUE}  \__        (|  /      /   /    
 \         \  /\\ __ {WHITE}/{BLUE}/\  /\  |\({WHITE}:{BLUE}   / {WHITE}"{BLUE}\      /|__/ \    /   /     
  {WHITE}\"{BLUE}____/\__\(__________)(__\_|_)\_______)    (_______)  |___/      

BY KELOMPOK 1 TA ALPRO 2022
{WHITE}''')

def get_selected_quiz(quiz_list):
  print('\nChoose a quiz to take:')
  for i, quiz in enumerate(quiz_list):
    print(f'{i + 1}. {quiz["subject"]} ({len(quiz["item_list"])} quiz)')

  choices = '/'.join([str(i + 1) for i in range(len(quiz_list))])
  quiz_index = int(input(f'{BLACK}({choices}){WHITE} ')) - 1
  return quiz_list[quiz_index]

def show_result(quiz, correct_answer_count):
  score = round(correct_answer_count / len(quiz['item_list']) * 100, 2)
  score_color = GREEN if score >= 70 else YELLOW if score >= 40 else RED
  
  print(f'\n{score_color}Correct answer:', correct_answer_count)
  print('Wrong answer:', len(quiz['item_list']) - correct_answer_count)
  print('Your score:', score)
  print(f'=============================={WHITE}')

def see_you():
  print(f'''{BLACK} ___  ____  ____    _  _  _____  __  __ 
/ __)( ___)( ___)  ( \/ )(  _  )(  )(  )
\__ \ )__)  )__)    \  /  )(_)(  )(__)( 
(___/(____)(____)   (__) (_____)(______)
{WHITE}''')

def play_quiz(quiz_list):
  quiz = get_selected_quiz(quiz_list)

  print(f'\nHave a good {quiz["subject"]} quiz:)')
  print('==============================\n')

  correct_answer_count = 0

  for i, item in enumerate(quiz['item_list']):
    print(f'{i + 1}) {item["question"]}')

    choice_list = []

    for key, choice in item['choice_dict'].items():
      choice_list.append(key)
      print(f'{key}. {choice}')

    choices = '/'.join(choice_list)
    answer = input(f'Answer: {BLACK}({choices}){WHITE} ').lower()
    if answer == item['answer']: correct_answer_count += 1
    print(f'{BLACK}------------------------------{WHITE}')

  show_result(quiz, correct_answer_count)

  play_again = input(f'Want to take the quiz again? {BLACK}(Y/n){WHITE} ').lower() != 'n'
  play_quiz(quiz_list) if play_again else see_you()

banner()
play_quiz(quiz_list)
