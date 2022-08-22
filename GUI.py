#Import needed tools
from WorkingWithData import DataFrame
from SentimentEngine import SentimentAnalyzer
import wx, wx.grid

#Create class for GUI
class Frame(wx.Frame):

    def __init__(self, *args, **kw):

        super(Frame, self).__init__(*args, **kw)

        #Panel setting
        self.panel = wx.Panel(self)

        #Main boxsizer setting
        self.main_boxsizer = wx.BoxSizer(orient = wx.VERTICAL)

        #Youtube link boxsizer setting
        self.youtube_link_boxsizer = wx.BoxSizer(orient = wx.HORIZONTAL)

        #TextCtrl setting
        self.youtube_link_textctrl = wx.TextCtrl(self.panel, id = wx.ID_ANY, value = "",
                                                 pos = wx.DefaultPosition, size = wx.Size(1180,20))
        self.youtube_link_textctrl.SetHint("Youtube link")

        #Button setting
        self.analyze_button = wx.Button(self.panel, id = wx.ID_ANY, label = "Analyze",
                                        pos = wx.DefaultPosition, size = wx.Size(60,20))

        #Button bind setting
        self.Bind(wx.EVT_BUTTON, self.AnalyzeComments, self.analyze_button)

        #Add widgets to Youtube link boxsizer setting
        self.youtube_link_boxsizer.Add(self.youtube_link_textctrl)
        self.youtube_link_boxsizer.AddSpacer(10)
        self.youtube_link_boxsizer.Add(self.analyze_button)

        #Comments grid setting
        self.comments_grid = wx.grid.Grid(self.panel, id = wx.ID_ANY,
                                          pos = wx.DefaultPosition, size = wx.Size(1260, 640))
        self.comments_grid.EnableEditing(False)
        self.comments_grid.SetRowLabelSize(0)
        self.comments_grid.CreateGrid(0,2)
        self.comments_grid.SetColLabelValue(0, "Author")
        self.comments_grid.SetColSize(0, 100)
        self.comments_grid.SetColLabelValue(1, "Comment")
        self.comments_grid.SetColSize(1, 1127)

        #Add widgets to main boxsizer
        self.main_boxsizer.Add(self.youtube_link_boxsizer, 0, wx.ALL, 10)
        self.main_boxsizer.Add(self.comments_grid, 0, wx.ALL, 10)

        #Frame setting
        self.panel.SetSizer(self.main_boxsizer)
        self.SetMinSize(wx.Size(1280,720))
        self.SetMaxSize(wx.Size(1280,720))

    #Analyze comments
    def AnalyzeComments(self, event):

        #Input path to the data
        path = "Comments.csv"

        #Create class for working with data
        df = DataFrame(path)

        #Create class for sentiment analysis
        sa = SentimentAnalyzer()

        #Get data from dataset
        comments = df.comments

        #Get polarity of the comments:
        data = sa.get_polarity(comments)

        #Clear data into the grid
        self.comments_grid.ClearGrid()

        #Add data to the grid
        for element in range(0, len(data)):
            self.comments_grid.AppendRows(1)
            self.comments_grid.SetCellValue(element, 1, data['comment_text'][element])
            if data['polarity'][element] == 1:
                self.comments_grid.SetCellBackgroundColour(element, 0, "Green")
                self.comments_grid.SetCellBackgroundColour(element, 1, "Green")
            if data['polarity'][element] == -1:
                self.comments_grid.SetCellBackgroundColour(element, 0, "Red")
                self.comments_grid.SetCellBackgroundColour(element, 1, "Red")
            if data['polarity'][element] == 0:
                self.comments_grid.SetCellBackgroundColour(element, 0, "Yellow")
                self.comments_grid.SetCellBackgroundColour(element, 1, "Yellow")
