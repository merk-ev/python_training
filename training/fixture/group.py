# Helper for group
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.filling(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit_first(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        # init edition
        self.select_first_group(wd)
        # open edit form
        wd.find_element_by_name("edit").click()
        # edit group form
        self.filling(new_group_data)
        # submit edit
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def filling(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if not text is None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_first_group(wd)
        # submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self, wd):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_groups_page(self):
         wd = self.app.wd
         wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
