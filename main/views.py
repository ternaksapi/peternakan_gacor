from django.shortcuts import render

# Create your views here.
products_data = [
    {
        'name': 'Padi',
        'description': 'Tanaman padi (Oryza sativa L.) adalah tanaman penghasil beras yang merupakan sumber karbohidrat bagi sebagian penduduk dunia',
        'amount': 30,
    },
    {
        'name': 'Jagung',
        'description': 'Tanaman jagung (Zea mays) adalah salah satu tanaman serealia penting di dunia dan digunakan untuk berbagai keperluan.',
        'amount': 40,
    },
    {
        'name': 'Daging Wagyu',
        'description': 'Daging wagyu adalah daging sapi yang berasal dari Jepang. Daging ini memiliki tekstur yang lembut dan lemak yang melimpah.',
        'amount': 5,
    },
    {
        'name': 'Susu Kambing',
        'description': 'Susu kambing adalah susu yang dihasilkan oleh kambing. Susu kambing memiliki kandungan nutrisi yang lebih tinggi dibandingkan dengan susu sapi.',
        'amount' : 0,
    },
    {
        'name': 'Telur Ayam',
        'description': 'Telur ayam adalah telur yang dihasilkan oleh ayam. Telur ayam memiliki kandungan nutrisi yang tinggi dan dapat dikonsumsi dalam berbagai bentuk.',
        'amount' : 60
    }
]

def show_main(request):
    context = {
        'products' : products_data,
    }

    return render(request, "main.html", context)