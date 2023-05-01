from PIL import Image, ImageDraw, ImageFont
import requests
import discord

class main:
    class Generate:
        @staticmethod
        async def welcome(member):
            # Open the user's profile picture
            profile_pic = Image.open(requests.get(member.avatar_url, stream=True).raw)
            profile_pic = profile_pic.resize((128, 128))

            # Create a blank image with the same dimensions as the background image
            bg_image = Image.new('RGB', (800, 400), color=(45, 48, 71))

            # Paste the user's profile picture onto the background image
            bg_image.paste(profile_pic, (100, 100))

            # Add the user's name and discriminator to the image
            draw = ImageDraw.Draw(bg_image)
            font = ImageFont.truetype('arial.ttf', size=40)
            text = f'Welcome, {member.name}#{member.discriminator}!'
            draw.text((300, 180), text, font=font, fill=(255, 255, 255))

            # Save the final image to a file
            bg_image.save('welcome.png')

            # Return the image as a file object
            with open('welcome.png', 'rb') as f:
                picture = discord.File(f)
                return picture
