from booking_scrap.booking import Booking

# try:
with Booking() as bot:
    bot.land_first_page()
    bot.where_we_going(destination="Larnaca")
    bot.when_we_going(check_in_date='22.12.2022', check_out_date='29.12.2022')
    #bot.when_we_going("2022-07-22", "2022-07-29")
    bot.who_is_going(3)
    bot.submit_data()
    bot.apply_filtrations()
    print("exiting...")
# except Exception as e:
#     if 'in PATH' in str(e):
#         print("You're trying to run the bot from command line \n You need to add path to your Selenium Drivers \n Windows: set PATH=%PATH%;C:path-to-your-folder \n Linux: PATH=$PATH:/path/toyour/folder \n")

#     else:
#         raise

