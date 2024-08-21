import requests
import pandas as pd

url = "https://cdn.casetify.com/api-cache/30m/Catalog2?artworkTags=%7B%7D&currency=USD&deviceShortName=iphone-15-pro-max&itemOptionTags=%7B%7D&lang=en_US&limit=960&offset=0&selectedTags=\\[%7B%22type%22:%22itemOptionTag%22,%22key%22:%22device_short_name%22,%22value%22:%22iphone-15-pro-max%22%7D\\]&sgmtB64=eNodlskRAyEMwBraB4cv%2Bm8sUh7RAD4wtmGz89vvO%2Bfr9b34zvR33uZ3%2BPWXO76868vaX%2Fb73upvr9nf3ofRzgJ1hdOXYr59dgqkV717txjxQDONtYDSuCGwiHBaf6AXrUo7baejyjhyjzxIU9vMA5owkth3KajzHyGt%2BwdmvRF0EFXnCNd033ME7mdhNjoYQxsjmBFkZL8jEpVXrD1iOWtdkQCzs65IUQXwfDZOAandG%2BXNUcGAcEQ2zrkiLQXnACFSlGgxQhUCAk6N4DynVu1ftvMUPASXFB9zD3AVes6LSpYjPVcgLTfqzaj%2F9Y8QeHlT3114vvsMwOxyBkBe7hmm1vLG%2FQOVyAQk5yZ5uUkf3FSaFOAm%2FQIcPVXouFuu9e3vmmeA2VsHaPb092iGWLRiLHaLRZsFvffFIfo4BEkAKdC7tE%2B4b7hl2LkA22wF7BFF1mirAUQQw9norQtIRAztHe%2FcL1claEfUI%2FcV5a2oAcQCUNkcBiA9rlmyvCqTHUCvpa2coUpQGRoWQcbhYh1v1ynBWrlRPabWA1wRwrXrVLOmwwBrszEbGjMnhZs%2Fcs9VYKNHuUEIIrWq%2BTR73uhXCjyMlQYtNKPmtejYWiSiFl5qNeB6Aypdm9yXOQCo7ImvvPFFUwJ24%2FYhuHq5rl3iq8seFdQXlMAfxRQKriNtqR6gZEXewUWZs35VNEOVW9q21dwtgD8TVk0mEToNR6kKbQuIoMkuwIE3vvr9gWA2I5MISrDvcA2AU734FNA4WyB4HtUuqWciXvxHePZ5KHNKZFv4tqLcZrIXZ%2BsVTqkgaFDqtdNWmSB7jcpsxJtVogVOfUGAa9c1XW36tA9FaR%2BF9j1oH4C%2B9EHfYMpNFOjdUkAVACNL0ea%2BQ1emncy5Vk5JcYexBD1JNkOwRxquNwo4dV9buUsHRA48vqXo1qz1ZwHIP2ZjaKYdOOK5Bv8RtmPMw%2BvYFoCXWQv3nVY6mnmEcd%2FxHFamrQxFZWRns89847sx5h78R65RBVCAko2lAFsoSFVwOj7cIEUJBBZgfAkB%2Fo6ej56PZofUcQLXKMBcvgbjCwyuwMvl%2FgKUL3kZn4e5pV6pp1NrNDyK4P1BBEHCxusywQFBCAWkGCglTWPxgIJxSkomKcX4vaST%2F0A5aVHyeoQqo8o4HaW8B5NunlQLqOyJyjB4CwBf0%2BE%2BCwXhmkks7jkIkaLEX6pyq6JnnzluVQhH5qrNEP0oUPYTPV7dsXOGbgDcWoCDsR6%2Bf8CRKfH%2B8g05wqmVHuPzOgP1DGjM%2BOh5%2Bg9VDOjx0RwfUDrqCNd073vKvwClFuC526NF55lT%2FxAALewN%2B29e%2F6Gt2X2W8bHHW8T8bEeQgPMCp%2FGfqoJTcISC1CL9B1YKSr1SrxT4783H4%2Fm1env9EQLp3o44BwfCbF9H8ceAv0U7IkhwhGuj7Sh4rj1taYHnS8Ppj0jh1IBOKaW%2Bzz8xfL8FuQL%2FESqX3PNgosd3G3A1%2BLuRP8GlGXc%3D&sorting=handpick&fn=query&version=20240821"

payload = {}
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'origin': 'https://www.casetify.com',
  'priority': 'u=1, i',
  'referer': 'https://www.casetify.com/',
  'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
phoneCaseData = response.json();
df = pd.json_normalize(phoneCaseData["data"]);
df.to_csv("phone_case_data.csv", index=False);
