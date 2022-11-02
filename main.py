import URLShorten_window_main
import logging

logging.basicConfig(filename = "URLShortenApp.log" , level = logging.INFO , format = '%(asctime)s %(levelname)s %(message)s')

def main():
    logging.info("URLShortenApp Opened")
    URLShorten_window_main.main()
    logging.info("URLShortenApp Closed")

if __name__ == '__main__':
    main()