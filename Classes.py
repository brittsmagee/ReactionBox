@client.command()
async def embedpages():
    page1 = discord.Embed (
        title = 'WARRIOR',
        description = 'Higher defense per level.',
        colour = discord.Colour.magenta()
    )
    page2 = discord.Embed (
        title = 'MAGE',
        description = 'Higher attack per level.',
        colour = discord.Colour.magenta()
    )
    page3 = discord.Embed (
        title = 'THIEF',
        description = 'Higher chance to steal money per level, with the $steal command.',
        colour = discord.Colour.magenta()
    )
    page4 = discord.Embed (
        title = 'RANGER',
        description = 'Have your pet hunt for items once every day, with the $hunt command.',
        colour = discord.Colour.magenta()
    )
    page5 = discord.Embed (
        title = 'RITUALIST',
        description = 'Higher chance to get loot items from adventures, higher favor reward from $pray and $sacrifice.',
        colour = discord.Colour.magenta()
	)
     page6 = discord.Embed (
        title = 'RAIDER',
        description = 'Higher $raidstats than usual. This is mainly useful if you participate in raids.',
        colour = discord.Colour.magenta()
	)
      page7 = discord.Embed (
        title = 'PARIOGON',
        description = 'Higher attack and defense per level.',
        colour = discord.Colour.magenta()
	)
    )

    pages = [page1, page2, page3, page4, page5, page6, page7]

    message = await client.say(embed = page1)

    await client.add_reaction(message, '⏮')
    await client.add_reaction(message, '◀')
    await client.add_reaction(message, '▶')
    await client.add_reaction(message, '⏭')

    i = 0
    emoji = ''

    while True:
        if emoji == '⏮':
            i = 0
            await client.edit_message(message, embed = pages[i])
        elif emoji == '◀':
            if i > 0:
                i -= 1
                await client.edit_message(message, embed = pages[i])
        elif emoji == '▶':
            if i < 2:
                i += 1
                await client.edit_message(message, embed = pages[i])
        elif emoji == '⏭':
            i = 2
            await client.edit_message(message, embed=pages[i])
        
        res = await client.wait_for_reaction(message = message, timeout = 30.0)
        if res == None:
            break
        if str(res[1]) != '<Reaction_Bot>':  #Example: 'MyBot#1111'
            emoji = str(res[0].emoji)
            await client.remove_reaction(message, res[0].emoji, res[1])

    await client.clear_reactions(message)
