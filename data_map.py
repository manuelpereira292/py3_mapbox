import plotly.graph_objects as go

latitude = 41.0253973
longitude = -8.5526033

mapbox_access_token = open("mapbox_token").read()

fig = go.Figure(go.Scattermapbox(lat = [latitude], lon = [longitude],
        mode='markers', marker=go.scattermapbox.Marker(
            size=10),text=['Home'],))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat= latitude,
            lon= longitude
        ),
        pitch=0,
        zoom=10
    )
)

fig.show()
