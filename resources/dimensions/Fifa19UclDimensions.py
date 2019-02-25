class Dimensions:
    def __init__(self):

        self.left_margin = 85
        self.left_margin_club_badge = self.left_margin + 10
        self.left_margin_overall = self.left_margin - 13

        self.top_margin_position = 195

        self.top_margin_name = 445

        self.top_margin_player_overall = 90

        '''
        Line separator dimensions
        '''
        self.top_margin_line_under_position = 255
        self.left_point_x_coordinate_line_under_position = self.left_margin + 20
        self.right_point_x_coordinate_line_under_position = self.left_point_x_coordinate_line_under_position + 55

        self.top_margin_line_under_country_flag = 335

        self.top_margin_line_under_name = 525
        self.margin_line_under_name = 90

        self.top_margin_vertical_line_between_stats_columns = self.top_margin_line_under_name + 20
        self.bottom_point_vertical_line_between_stats_columns = self.top_margin_vertical_line_between_stats_columns + 165

        self.top_margin_line_under_stats = 735
        self.margin_line_under_stats = 300

        self.attr_value_label_horizontal_gap = 70

        self.left_margin_attr_value_col1 = self.left_margin + 0
        self.left_margin_attr_label_col1 = self.left_margin_attr_value_col1 + self.attr_value_label_horizontal_gap

        self.left_margin_attr_value_col2 = self.left_margin_attr_value_col1 + 220
        self.left_margin_attr_label_col2 = self.left_margin_attr_value_col2 + self.attr_value_label_horizontal_gap

        self.stats_row_vertical_gap = 62

        self.top_margin_label_offset = 3

        self.top_margin_stats_row_1_values = 530
        self.top_margin_stats_row_1_labels = self.top_margin_stats_row_1_values + self.top_margin_label_offset

        self.top_margin_stats_row_2_values = self.top_margin_stats_row_1_values + self.stats_row_vertical_gap
        self.top_margin_stats_row_2_labels = self.top_margin_stats_row_2_values + self.top_margin_label_offset

        self.top_margin_stats_row_3_values = self.top_margin_stats_row_2_values + self.stats_row_vertical_gap
        self.top_margin_stats_row_3_labels = self.top_margin_stats_row_3_values + self.top_margin_label_offset

        self.left_margin_player_image = 165
        self.left_margin_dynamic_player_image = 30
        self.bottom_margin_dynamic_player_image = 170
