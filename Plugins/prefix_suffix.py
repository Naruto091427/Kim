from pyrogram import Client, filters, enums
from helper.database import Kim_Dokja14


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Prefix__\n\nExample:- `/set_prefix @Kim_Dokja14`**")
    prefix = message.text.split(" ", 1)[1]
    Kim Dokja = await message.reply_text("Please Wait ...")
    await Kim_Dokja14.set_prefix(message.from_user.id, prefix)
    await Kim Dokja.edit("**Prefix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    Kim Dokja = await message.reply_text("Please Wait ...")
    prefix = await Kim_Dokja14.get_prefix(message.from_user.id)
    if not prefix:
        return await Kim Dokja.edit("**You Don't Have Any Prefix ❌**")
    await Kim_Dokja14.set_prefix(message.from_user.id, None)
    await Kim Dokja.edit("**Prefix Deleted Successfully 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    KimDokja = await message.reply_text("Please Wait ...")
    prefix = await Kim_Dokja14.get_prefix(message.from_user.id)
    if prefix:
        await KimDokja.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await KimDokja.edit("**You Don't Have Any Prefix ❌**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**__Give The Suffix__\n\nExample:- `/set_suffix @Kim_Dokja14`**")
    suffix = message.text.split(" ", 1)[1]
    KimDokja = await message.reply_text("Please Wait ...")
    await Kim_Dokja14.set_suffix(message.from_user.id, suffix)
    await KimDokja.edit("**Suffix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    KimDokja = await message.reply_text("Please Wait ...")
    suffix = await Kim_Dokja14.get_suffix(message.from_user.id)
    if not suffix:
        return await KimDokja.edit("**You Don't Have Any Suffix ❌**")
    await Kim_Dokja14.set_suffix(message.from_user.id, None)
    await KimDokja.edit("**Suffix Deleted Successfully ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    KimDokja = await message.reply_text("Please Wait ...")
    suffix = await Kim_Dokja14.get_suffix(message.from_user.id)
    if suffix:
        await KimDokja.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await KimDokja.edit("**You Don't Have Any Suffix ❌**")











