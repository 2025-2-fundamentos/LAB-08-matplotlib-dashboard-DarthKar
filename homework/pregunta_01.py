# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import os
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")  
    import matplotlib.pyplot as plt


    os.makedirs(os.path.join('docs'), exist_ok=True)


    df = pd.read_csv(os.path.join('files', 'input', 'shipping-data.csv'))

    # --- Shippings per Warehouse ---
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title='Shippings per Warehouse',
        xlabel='Warehouse block',
        ylabel='Record Count',
        color='tab:blue',
        fontsize=8
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig(os.path.join('docs', 'shipping_per_warehouse.png'))

    # --- Mode of shipment ---
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title='Mode of shipment',
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue", "tab:orange", "tab:green"]
    )
    plt.savefig(os.path.join('docs', 'mode_of_shipment.png'))

    # --- Average Customer Rating ---
    plt.figure()
    rate = (
        df[['Mode_of_Shipment', 'Customer_rating']]
        .groupby("Mode_of_Shipment")
        .describe()
    )
    rate.columns = rate.columns.droplevel()
    rate = rate[["mean", 'min', 'max']]

    plt.barh(
        y=rate.index.values,
        width=rate['max'].values - 1,
        left=rate['min'].values,
        height=0.9,
        color='lightgray',
        alpha=0.8
    )
    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in rate["mean"].values
    ]
    plt.barh(
        y=rate.index.values,
        width=rate['mean'].values - 1,
        left=rate['min'].values,
        height=0.5,
        color=colors,
        alpha=1.0
    )
    plt.title('Average Customer Rating')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_color('grey')
    plt.gca().spines['left'].set_color('grey')
    plt.savefig(os.path.join('docs', 'average_customer_rating.png'))

    # --- Shipped Weight Distribution ---
    plt.figure()
    df.Weight_in_gms.hist(
        color='lightgreen',
        edgecolor='black',
        grid=False
    )
    plt.title('Shipped Weight Distribution')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig(os.path.join('docs', 'weight_distribution.png'))

pregunta_01()