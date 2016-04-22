import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import Scatter, Data, Stream, Figure, Layout

def forward(configuration, readings):
    print("Plotlying... {0}.".format(readings))
    # TODO We need a process running in continue to stream
    # to Plotly. We really do need to implement the forwarding
    # with an independant app, dispatching readings coming from a broker.
    py.sign_in(configuration['plotly']['username'],
        configuration['plotly']['apiKey'])
    url = py.plot(
        Figure(
            layout=Layout(
                title=configuration['plotly']['plotTitle'],
                xaxis=dict(title='Timestamp'),
                yaxis=dict(title='Dose (uSv/h)')),
            data=Data([
                Scatter(
                    x=[], y=[],
                    mode='lines',
                    stream=Stream(
                        token=configuration['plotly']['streamingToken']))])),
        filename=configuration['plotly']['plotTitle'])
    print("Plotly graph URL: {0}".format(url))
    stream = py.Stream(configuration['plotly']['streamingToken'])
    stream.open()
    stream.write(dict(x=readings['timestamp'], y=readings['uSvh']))
    stream.close()
    print("Plotly Ok.")
