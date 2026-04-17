import argparse as ap
from requests_html import HTMLSession
import asyncio
import python_weather
parser = ap.ArgumentParser(description='get the weather for an area')
parser.add_argument('--prompt')
args = parser.parse_args()
prompt = args.prompt
prompt = prompt.split(' in ')[1]
print(prompt)
async def main() -> None:
  
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    
    weather = await client.get(f'{prompt}')
    
    print(weather.temperature)
    
if __name__ == '__main__':
  asyncio.run(main())

