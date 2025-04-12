from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.button import MDRaisedButton


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create main layout
        main_layout = MDBoxLayout(orientation="vertical")
        
        # Create navbar
        navbar = MDBoxLayout(
            size_hint_y=None,
            height="64dp",
            md_bg_color=(0.78, 0.8, 0.8666, 1),
            padding=["10dp", 0, "10dp", 0]
        )
        
        # Add navbar elements
        menu_button = MDIconButton(
            icon="menu",
            size_hint_x=None,
            width="48dp",
            pos_hint={"center_y": .5}
        )
        
        title = MDLabel(
            text="BetterExam™",
            font_style="H6",
            halign="center"
        )
        
        profile_button = MDIconButton(
            icon="account-circle",
            size_hint_x=None,
            width="48dp",
            pos_hint={"center_y": .5}
        )
        
        navbar.add_widget(menu_button)
        navbar.add_widget(title)
        navbar.add_widget(profile_button)
        
        # Create a scroll view for content
        scroll_view = MDScrollView(
            do_scroll_x=False,  # Only scroll vertically
            size_hint=(1, 1)    # Take all available space below navbar
        )
        
        # Create content layout with padding
        content_layout = MDBoxLayout(
            orientation="vertical",
            padding="10dp",
            spacing="10dp",
            size_hint_y=None  # Important for scrolling
        )
        # Bind the height of content_layout to its minimum height
        # This makes it expand based on children
        content_layout.bind(minimum_height=content_layout.setter('height'))
        
        # Create card
        card = MDCard(
            orientation="vertical",
            padding="0dp",
            size_hint=(0.9, None),  # Fixed width, adaptive height
            size_hint_min_y=None,   # Allow minimum height
            pos_hint={"center_x": 0.5},
            elevation=2,
            radius=[15, 15, 15, 15]  # Adding rounded corners to the card
        )
        # Bind card height to its minimum height so it expands with content
        card.bind(minimum_height=card.setter('height'))
        
        # Create card header with back button
        card_header = MDBoxLayout(
            size_hint_y=None,
            height="48dp",
            md_bg_color=(0.78, 0.8, 0.8666, 1),
            padding=["10dp", 0, "10dp", 0],
            radius=[15, 15, 0, 0]  # Rounded corners only at the top
        )
        
        # Back button - positioned on the left side of header
        back_button = MDIconButton(
            icon="arrow-left-circle",
            theme_icon_color="Custom",
            icon_color=(1, 1, 1, 1),  # White to match header text
            size_hint_x=None,
            width="100dp",  # Increased width for a bigger button
            height="100dp",  # Added height to make it proportional
            pos_hint={"center_y": .5}
        )
        
        header_title = MDLabel(
            text="#1234 Basics of Linux",
            theme_text_color="Primary",
            text_color=(1, 1, 1, 1),
            font_style="H6"
        )
        
        # Add both to header
        card_header.add_widget(back_button)
        card_header.add_widget(header_title)
        
        # Create card content area with padding
        card_content = MDBoxLayout(
            orientation="vertical",
            padding="10dp",
            spacing="10dp",
            size_hint_y=None,  # Important - allows height to be calculated
            md_bg_color=(1, 1, 1, 1)  # White background for content area
        )
        # Bind card_content height to its minimum height
        card_content.bind(minimum_height=card_content.setter('height'))

        # Professor (now without the back button)
        professor_label = MDLabel(
            text="[b]Professor[/b]: Jane Doe",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(professor_label)

        # Contact
        contact_label = MDLabel(
            text="[b]Contact[/b]: [u]user@lut.fi[/u]",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(contact_label)

        # Exam type
        exam_type_label = MDLabel(
            text="[b]Exam type[/b]: paper",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(exam_type_label)

        # Description
        description_label = MDLabel(
            text="[b]Description[/b]:",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(description_label)

        # Description card
        description_card = MDCard(
            orientation="vertical",
            padding="10dp",
            spacing="5dp",
            size_hint_y=None,  # Important for correct height calculation
            md_bg_color=(0.98, 0.98, 0.98, 1),
            elevation=2
        )
        # Bind the height of description_card to its minimum height
        description_card.bind(minimum_height=description_card.setter('height'))
        
        description_items = [
            "- Exam focuses on the practical part of topics 4-8 and the theoretical part of topics 1-3, 8-12",
            "- 8 Multiple choice questions (20p)",
            "- 12 Short answer questions (80p)"
        ]
        
        for item in description_items:
            item_label = MDLabel(
                text=item,
                font_style="Body2",
                size_hint_y=None,
                height="30dp"
            )
            description_card.add_widget(item_label)
            
        card_content.add_widget(description_card)

        # Instructions
        instructions_label = MDLabel(
            text="[b]Instructions[/b]:",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(instructions_label)

        # Instructions card
        instructions_card = MDCard(
            orientation="vertical",
            padding="10dp",
            spacing="5dp",
            size_hint_y=None,  # Important for correct height calculation
            md_bg_color=(0.98, 0.98, 0.98, 1),
            elevation=2
        )
        # Bind the height of instructions_card to its minimum height
        instructions_card.bind(minimum_height=instructions_card.setter('height'))
        
        instruction_items = [
            "- only pen / pencil and eraser allowed",
            "- bring ID (or other proof of identity)"
        ]
        
        for item in instruction_items:
            item_label = MDLabel(
                text=item,
                font_style="Body2",
                size_hint_y=None,
                height="30dp"
            )
            instructions_card.add_widget(item_label)
            
        card_content.add_widget(instructions_card)

        # Date
        date_label = MDLabel(
            text="[b]Date[/b]: 26 / 01 / 2025",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(date_label)

        # Duration
        duration_label = MDLabel(
            text="[b]Duration[/b]: 16:30 - 19:30 (3 hours)",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(duration_label)

        # Location
        location_label = MDLabel(
            text="[b]Location[/b]: Lahti",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(location_label)

        # Exam room
        exam_room_label = MDLabel(
            text="[b]Exam room[/b]: M_AUD2B",
            markup=True,
            font_style="Body1",
            size_hint_y=None,
            height="30dp"
        )
        card_content.add_widget(exam_room_label)
        
        # Add header and content to card
        card.add_widget(card_header)
        card.add_widget(card_content)
        
        # Add card to content layout
        content_layout.add_widget(card)
        
        # Add cancel button
        cancel_button = MDRaisedButton(
            text="Cancel Reservation",
            md_bg_color=(232/255, 95/255, 96/255, 1),  # Red color
            pos_hint={"center_x": 0.5},
            size_hint=(0.5, None),
            height="48dp",
            padding=("20dp", "10dp"),
            rounded_button=True,
            elevation=2
        )
        content_layout.add_widget(cancel_button)
        
        # Add content_layout to the scroll view
        scroll_view.add_widget(content_layout)
        
        # Add widgets to main layout
        main_layout.add_widget(navbar)
        main_layout.add_widget(scroll_view)
        
        self.add_widget(main_layout)


class CardApp(MDApp):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    CardApp().run()