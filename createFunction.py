import folium.plugins
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import folium

def create_price_map(df, lat, lng, price, size, income, filename="Untitled"):
    m = folium.Map(location=[df[lat].mean(), df[lng].mean()], zoom_start=5)
    
    price_max, price_min = df[price].max(), df[price].min()
    size_max, size_min = df[size].max(), df[size].min()
    
    for _, row in df.iterrows():
        normalized_price = (row[price] - price_min) / (price_max - price_min)
        normalized_size = (row[size] - size_min) / (size_max - size_min)
        colour = plt.cm.RdYlGn(1 - normalized_price)
        
        popup_info = f"""
        House Value: ${normalized_price:2f}<br>
        Average Size: {normalized_size}<br>
        Population: {row['Population']}<br>
        Income: ${row[inc]:.2f}
        """
        
        folium.CircleMarker(
            location = [row[lat], row[lng]],
            radius = 5,
            color = mcolors.to_hex(colour[:3]),
            fill=True,
            fill_color = mcolors.to_hex(colour[:3]),
            fill_opacity = 0.75,
            popup = folium.Popup(popup_info, max_width=500)
        ).add_to(m)
        
    folium.plugins.MiniMap().add_to(m)
    
    m.save(f"{filename}_price_map.html")
    
    return