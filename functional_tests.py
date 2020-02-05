from selenium import webdriver

browser = webdriver.Firefox()

# Alice loads our web site.
browser.get('http://localhost:8000')

# She sees that she can track tasks.
assert 'Tasks' in browser.title

# She sees a call to action.

# She enters a task: Buy a skateboard.

# When she hits enter, a page shows her task.

# She enters another: Go skateboarding.

# The site says she can see the list at its own URL.

# She visits the URL, the list is there.

browser.quit()
