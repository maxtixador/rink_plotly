import numpy as np
import plotly.graph_objects as go

class Rink:

    def __init__(self, setting="full", vertical=False):
        self.setting = setting
        self.direction = "vertical" if vertical else "horizontal"
        self.fig = go.Figure()


    def _faceoff_circle(self, x, y):
        '''
        Function to plot faceoff circles in Plotly. Takes 2 arguments :
        x : x coordinate of the center of the circle
        y : y coordinate of the center of the circle
        '''

        theta = np.linspace(0, 2*np.pi, 300)
        # Outer circle
        x_outer = x + 15*np.cos(theta)
        y_outer = y + 15*np.sin(theta)
        outer_circle = go.Scatter(x=x_outer, y=y_outer, mode='lines', line=dict(width=2, color='red'), showlegend=False, hoverinfo='skip')
        # Inner circle
        x_inner = x + np.cos(theta)
        y_inner = y + np.sin(theta)
        inner_circle = go.Scatter(x=x_inner, y=y_inner, mode='lines', fill='toself', fillcolor='rgba(255, 0, 0, 0.43)', line=dict(color='rgba(255, 0, 0, 1)', width=2), showlegend=False, hoverinfo='skip')
        self.fig.add_traces([outer_circle, inner_circle])

    def _goal_crease(self,flip=1, vertical = False):
        '''
        Function to plot goal crease in Plotly. Takes 1 argument :
        vertical : True if you want a vertical rink, False (default) is for an horizontal rink
        '''

        # Dictionary of settings for vertical and horizontal rinks
        settings = {"vertical" : {
            "x" : np.concatenate(([-4], np.linspace(-4, 4, 100), [4])),
            "y" : flip * np.concatenate(([89], 83 + np.linspace(-4, 4, 100)**2/4**2*1.5, [89])),
        },
        "horizontal" : {
            "x" : flip * np.concatenate(([89], 83 + np.linspace(-4, 4, 100)**2/4**2*1.5, [89])),
            "y" : np.concatenate(([-4], np.linspace(-4, 4, 100), [4])),
        }
        }

        # Selecting the right settings
        gc_settings = settings["vertical"] if self.direction == "vertical" else settings["horizontal"]
        
        self.fig.add_trace(go.Scatter(x = gc_settings["x"],
                                    y = gc_settings["y"],
                                    fill = 'toself',
                                    fillcolor = 'rgba(173, 216, 230, 0.3)',
                                    line = dict(color='red'),
                                    showlegend = False,
                                    hoverinfo = 'skip'))

    def _define_layout(self):
        '''
        Function to define layout in Plotly. Takes 1 argument :
        vertical : True if you want a vertical rink, False (default) is for a horizontal rink
        '''
        settings = {
            "full": [-101, 101],
            "offense": [0, 101],
            "ozone": [25, 101],
            "defense": [-101, 0],
            "dzone": [-101, -25],
            "neutral": [-25, 25]
        }

        common_layout = {
            "xaxis": dict(showgrid=False, zeroline=False, showticklabels=False),
            "yaxis": dict(showgrid=False, zeroline=False, showticklabels=False, constrain="domain"),
            "autosize": True,
            "template": "plotly_white"
        }

        if self.direction == "vertical":
            common_layout["xaxis"].update(range=[-42.6, 42.6])
            common_layout["yaxis"].update(range=settings[self.setting])
        else:
            common_layout["xaxis"].update(range=settings[self.setting])
            common_layout["yaxis"].update(range=[-42.6, 42.6])


        self.fig.update_layout(**common_layout)
        self.fig.update_yaxes(scaleanchor="x", scaleratio=1)


    def _outer_circle(self):
        '''
        Function to plot outer circle in Plotly. Takes 2 arguments :
        fig : figure object
        vertical : True if you want a vertical rink, False (default) is for a horizontal rink
        '''

        theta = np.linspace(0, 2*np.pi, 300)
        x_outer = 15 * np.cos(theta) if self.direction == "vertical" else 15 * np.sin(theta)
        y_outer = 15 * np.sin(theta) if self.direction == "vertical" else 15 * np.cos(theta)
        self.fig.add_trace(go.Scatter(x=x_outer, y=y_outer, mode='lines', line=dict(color='royalblue', width=2), showlegend=False, hoverinfo='skip'))

    def _inner_circle(self):
        '''
        Function to plot inner circle in Plotly. Takes 2 arguments :
        fig : figure object
        vertical : True if you want a vertical rink, False (default) is for a horizontal rink
        '''

        theta2 = np.linspace(np.pi/2, 3*np.pi/2, 300)
        x_inner = 42.5 + 10 * np.cos(theta2) if self.direction == "vertical" else 10 * np.sin(theta2)
        y_inner = 10 * np.sin(theta2) if self.direction == "vertical" else -42.5 - 10 * np.cos(theta2)
        self.fig.add_trace(go.Scatter(x=x_inner, y=y_inner, mode='lines', line=dict(color='red', width=2), showlegend=False, hoverinfo='skip'))

    def _rink_boundaries(self):
        '''
        Function to plot rink boundaries in Plotly. Takes 2 arguments :
        fig : figure object
        vertical : True if you want a vertical rink, False (default) is for a horizontal rink
        '''
        if self.direction == "vertical" :
            self.fig.add_shape(type='rect', xref='x', yref='y', x0=-42.5, y0=25, x1=42.5, y1=26, line=dict(color='royalblue', width=1), fillcolor='royalblue', opacity=1)
            self.fig.add_shape(type='rect', xref='x', yref='y', x0=-42.5, y0=-25, x1=42.5, y1=-26, line=dict(color='royalblue', width=1), fillcolor='royalblue', opacity=1)
            self.fig.add_shape(type='rect', xref='x', yref='y', x0=-42.5, y0=-0.5, x1=42.5, y1=0.5, line=dict(color='red', width=2), fillcolor='red')

        else :
            # Rink boundaries
            self.fig.add_shape(type='rect', xref='x', yref='y', x0=25, y0=-42.5, x1=26, y1=42.5, line=dict(color='royalblue', width=1), fillcolor='royalblue', opacity=1)
            self.fig.add_shape(type='rect', xref='x', yref='y', x0=-25, y0=-42.5, x1=-26, y1=42.5, line=dict(color='royalblue', width=1), fillcolor='royalblue', opacity=1)
            self.fig.add_shape(type='rect', xref='x', yref='y', x0=-0.5, y0=-42.5, x1=0.5, y1=42.5, line=dict(color='red', width=2), fillcolor='red')



    def _goal_line(self):
        '''
        Function to plot goal line in Plotly. Takes 2 arguments :
        fig : figure object
        vertical : True if you want a vertical rink, False (default) is for a horizontal rink
        '''

        if self.direction == "vertical":
            goal_line_extreme = 42.5 - 28 + np.sqrt(28**2 - (28-11)**2)
            self.fig.add_shape(type='line', xref='x', yref='y', x0=-goal_line_extreme, y0=89, x1=goal_line_extreme, y1=89, line=dict(color='red', width=2))
            self.fig.add_shape(type='line', xref='x', yref='y', x0=-goal_line_extreme, y0=-89, x1=goal_line_extreme, y1=-89, line=dict(color='red', width=2))
        else:
            goal_line_extreme = 42.5 - 28 + np.sqrt(28 ** 2 - (28 - 11) ** 2)
            self.fig.add_shape(type='line', xref='x', yref='y', x0=89, y0=-goal_line_extreme, x1=89, y1=goal_line_extreme, line=dict(color='red', width=2))
            self.fig.add_shape(type='line', xref='x', yref='y', x0=-89, y0=-goal_line_extreme, x1=-89, y1=goal_line_extreme, line=dict(color='red', width=2))


    def _sidelines(self):
        '''
        Function to plot sidelines in Plotly. Takes 2 arguments :
        fig : figure object
        vertical : True if you want a vertical rink, False (default) is for a horizontal rink
        '''
        if self.direction == "vertical" :
            theta_lines = np.linspace(0, np.pi/2, 20)
            x_lines1 = np.concatenate(([-42.5], -42.5 + 28 - 28*np.cos(theta_lines), 42.5 - 28 + 28*np.cos(np.flip(theta_lines))))
            y_lines1 = np.concatenate(([15], 72 + 28*np.sin(theta_lines), 72 + 28*np.sin(np.flip(theta_lines))))
            x_lines2 = np.concatenate(([-42.5], -42.5 + 28 - 28*np.cos(theta_lines), 42.5 - 28 + 28*np.cos(np.flip(theta_lines))))
            y_lines2 = np.concatenate(([15], -72 - 28*np.sin(theta_lines), -72 - 28*np.sin(np.flip(theta_lines))))
            self.fig.add_trace(go.Scatter(x=x_lines1, y=y_lines1, mode='lines', line=dict(color='black', width=2), showlegend=False, hoverinfo='skip'))
            self.fig.add_trace(go.Scatter(x=x_lines2, y=y_lines2, mode='lines', line=dict(color='black', width=2), showlegend=False, hoverinfo='skip'))
            self.fig.add_shape(type='line', xref='x', yref='y', x0=42.5, y0=-72.5, x1=42.5, y1=72.5, line=dict(color='black', width=2))
            self.fig.add_shape(type='line', xref='x', yref='y', x0=-42.5, y0=-72.5, x1=-42.5, y1=72.5, line=dict(color='black', width=2))
        else :
            theta_lines = np.linspace(0, np.pi / 2, 20)
            x_lines1 = np.concatenate(([15], 72 + 28 * np.sin(theta_lines), 72 + 28 * np.sin(np.flip(theta_lines))))
            y_lines1 = np.concatenate(([-42.5], -42.5 + 28 - 28 * np.cos(theta_lines), 42.5 - 28 + 28 * np.cos(np.flip(theta_lines))))
            x_lines2 = np.concatenate(([15], -72 - 28 * np.sin(theta_lines), -72 - 28 * np.sin(np.flip(theta_lines))))
            y_lines2 = np.concatenate(([-42.5], -42.5 + 28 - 28 * np.cos(theta_lines), 42.5 - 28 + 28 * np.cos(np.flip(theta_lines))))
            self.fig.add_trace(go.Scatter(x=x_lines1, y=y_lines1, mode='lines', line=dict(color='black', width=2), showlegend=False, hoverinfo='skip'))
            self.fig.add_trace(go.Scatter(x=x_lines2, y=y_lines2, mode='lines', line=dict(color='black', width=2), showlegend=False, hoverinfo='skip'))
            self.fig.add_shape(type='line', xref='x', yref='y', x0=-72.5, y0=-42.5, x1=72.5, y1=-42.5, line=dict(color='black', width=2))
            self.fig.add_shape(type='line', xref='x', yref='y', x0=-72.5, y0=42.5, x1=72.5, y1=42.5, line=dict(color='black', width=2))

    
    def plot(self):
        '''
        Function to plot rink in Plotly.
        '''

        self._define_layout()
        self._rink_boundaries()
        self._outer_circle()
        self._inner_circle()
        self._goal_line()
        self._sidelines()
        self._goal_crease(flip=1)
        self._goal_crease(flip=-1)


        if self.direction == "vertical" :
            self._faceoff_circle(-22, 69)
            self._faceoff_circle(22, 69)
            self._faceoff_circle(-22, -69)
            self._faceoff_circle(22, -69)

        else :
            self._faceoff_circle(-69, -22)
            self._faceoff_circle(-69, 22)
            self._faceoff_circle(69, -22)
            self._faceoff_circle(69, 22)
            
            

        return self.fig.show()


# Example usage:
rink = Rink(setting="full", vertical=True)
rink.plot()
