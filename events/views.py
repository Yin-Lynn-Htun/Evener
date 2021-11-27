from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import date

import events

# Create your views here.


dummy_events = [
    {
        'id': 1,
        'name': 'Brithday Party',
        'location': "Novotel Hotel",
        'registered': 12 ,
        'organizer': 'William',
        'date': date(2020, 1, 21),
        'detail': """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer lacinia auctor leo at posuere. Sed ipsum augue, semper quis mi ut, tempus auctor nulla. Integer dapibus nec est in luctus. Cras porttitor ultrices porttitor. Fusce sit amet felis sed sapien interdum rhoncus. Sed vitae nisi sit amet neque sagittis pharetra nec sit amet sem. Nullam ornare urna sit amet accumsan fermentum. Proin risus nisl, fermentum at erat vel, imperdiet sodales sapien. Nunc elit leo, sollicitudin at molestie vel, sodales ac augue. Sed porttitor lectus pellentesque hendrerit feugiat. Mauris nulla nibh, blandit ac diam at, ornare pretium leo. Phasellus placerat mollis tempus. Mauris vel augue ut orci lobortis iaculis ac et enim. Aliquam luctus justo eget justo iaculis, eu vestibulum dui iaculis.

            Integer id velit sed dui fringilla imperdiet eu ac lacus. Donec in ante eu orci iaculis euismod vitae ac diam. Quisque dignissim, diam in interdum lacinia, ante est interdum dui, a posuere orci diam non dolor. Aenean non enim ornare, molestie risus sit amet, interdum est. Suspendisse fringilla ornare dolor, at tempor erat sollicitudin ut. Praesent rutrum vehicula orci vitae volutpat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Integer sagittis eleifend ex et sollicitudin. Morbi vel lorem vel nunc feugiat mollis eget vitae purus. Pellentesque est sem, ultricies a quam quis, cursus posuere dui. Sed nec sodales massa, egestas iaculis ante. Quisque dictum eros erat, ac condimentum enim sodales et. Maecenas rhoncus maximus aliquet. Suspendisse sed eros tincidunt, ullamcorper risus id, venenatis velit. Mauris vulputate orci et iaculis iaculis.

            Morbi porta eros at pharetra iaculis. Sed ut ultrices orci. Praesent metus orci, mattis vel tellus sed, pellentesque faucibus arcu. Nunc vel nibh ut erat ornare fringilla ultrices sed libero. Donec eget tempus enim. Praesent hendrerit varius pulvinar. Cras convallis facilisis diam, quis luctus turpis. Maecenas elementum pretium enim ut faucibus. Cras felis sapien, efficitur at suscipit non, fermentum at elit. Integer ac dapibus quam.

            Aenean nisl mauris, consequat ac massa quis, varius mattis eros. Mauris purus est, vulputate in ullamcorper a, commodo at purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam vitae odio in lectus euismod maximus at eu purus. Duis imperdiet et mauris sed faucibus. Nullam id lorem sit amet erat pellentesque ornare in congue enim. Mauris eleifend mauris sed velit pretium suscipit. Proin malesuada elit dictum, consequat dolor vitae, malesuada orci. Vivamus justo enim, bibendum et ex vel, auctor mattis nisi. Duis suscipit lectus in lobortis dictum.

            Praesent ut diam in nisi dictum convallis. Vestibulum diam quam, volutpat et rhoncus id, pellentesque a nulla. Mauris vel enim at orci sodales pellentesque et quis orci. Fusce at mauris massa. Phasellus at lacinia augue, rhoncus pulvinar quam. Sed vitae ligula a velit condimentum varius. Cras condimentum, lectus et consectetur luctus, justo tortor tempor libero, eu sagittis odio justo vitae dolor. Suspendisse in luctus metus. Sed augue justo, euismod quis maximus eu, ornare vitae diam. Donec tristique, arcu in interdum scelerisque, massa augue mollis urna, nec porta odio neque a lorem. Aenean laoreet accumsan lacus nec auctor.
        """
    },

    {
        'id': 2,
        'name': 'EDM Music festival',
        'location': "Summer park",
        'date': date(2020, 4, 20),
        'registered': 30,
        'organizer': 'James',
        'detail': """
            Ut commodo nibh in tortor tristique sollicitudin. Nulla felis sapien, bibendum quis magna eu, maximus tristique erat. Cras dictum volutpat placerat. Nullam sollicitudin sagittis dictum. Nam pharetra nulla a efficitur convallis. Quisque pharetra posuere augue quis vulputate. Nulla facilisi. Nulla nec augue et mi pharetra fringilla. Nam elit libero, sollicitudin sit amet diam non, dignissim dignissim nisl. In eu velit nulla. Donec ac pellentesque eros, sit amet semper arcu. Morbi consectetur risus ac euismod aliquet.

            Nulla rhoncus cursus ex. Phasellus ac molestie enim. Suspendisse nisl justo, ullamcorper sit amet leo eget, dignissim semper risus. Maecenas ac arcu aliquet, placerat nisi in, ultrices erat. Praesent lacus lacus, facilisis quis lectus id, pretium fringilla urna. Morbi felis urna, iaculis eu laoreet id, consectetur sed sem. Integer sagittis sed libero quis ullamcorper. Aliquam vitae ex bibendum, rutrum sem vel, gravida diam. Etiam mi velit, porttitor in consectetur ac, rutrum sed tellus. Praesent rutrum turpis vel fringilla commodo. Duis eget neque libero. Cras efficitur erat non risus scelerisque, id interdum libero porttitor. Ut blandit lobortis congue.

            Proin lacinia, arcu ac pharetra tempor, nulla nisi tincidunt leo, in ullamcorper nisl ipsum a erat. In finibus, urna sit amet porttitor sodales, sem sem sodales eros, eu pharetra ligula lectus id odio. Sed placerat libero in diam congue, in ornare justo euismod. Mauris vestibulum magna id est dignissim tempor. Duis eu urna ut quam commodo facilisis nec sit amet odio. Mauris ultrices blandit mi, sed accumsan orci suscipit vitae. Praesent fringilla porttitor euismod. Ut rutrum vestibulum magna non cursus. Vivamus molestie ante viverra elit tincidunt, in maximus risus ornare. Vivamus sapien arcu, ornare et ultrices eu, elementum vitae nunc. Pellentesque purus leo, efficitur vel metus eu, faucibus fringilla urna. Etiam at semper enim, ullamcorper mattis erat. Nulla metus erat, fringilla vitae ligula a, volutpat semper tellus. Nullam mollis, libero ac feugiat malesuada, urna enim malesuada odio, eget ornare dolor risus sit amet risus. Sed accumsan leo nec lectus porta, at auctor purus feugiat.
        """
    },

     {
        'id': 3,
        'name': 'Wedding Party',
        'location': 'Sedona Hotel',
        'date': date(2020, 7, 20),
        'registered': 10,
        'organizer': 'Liam',
        'detail': """
            Aliquam erat volutpat. Sed efficitur mi ut congue eleifend. Etiam blandit fringilla magna, eu interdum diam consequat aliquet. Integer nec maximus eros, in maximus felis. Sed tincidunt urna ipsum, aliquam bibendum purus bibendum eu. Nullam ut faucibus nulla, ut mattis leo. Quisque luctus porttitor nisi, ultricies ultrices ipsum ornare et. Donec turpis sem, condimentum non iaculis nec, varius eget metus. Aliquam vitae sodales dui, eu dapibus est. Sed lobortis, mauris vitae rhoncus pretium, risus nisl posuere magna, ut pulvinar lectus justo at augue. Aenean a diam ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur laoreet quam nec lorem iaculis, in egestas ipsum fermentum. Aliquam dictum diam magna, volutpat hendrerit massa venenatis ut.

            Mauris congue, dolor ornare sagittis varius, augue ante lobortis quam, non convallis nulla felis eget quam. Duis nisi sapien, eleifend sagittis pulvinar et, iaculis ut velit. Nulla facilisi. Aenean aliquam augue lorem, non semper elit tincidunt vel. Cras id cursus augue. Praesent nec aliquet sapien. Maecenas a facilisis elit. Cras egestas felis a justo maximus accumsan. Sed non tristique quam, nec auctor justo. Nulla varius, libero eget rutrum congue, odio nisl mollis ante, vel viverra lacus purus nec sapien.

            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Consequatur tempore, perspiciatis nostrum eaque quia magnam neque ad soluta? Adipisci, sunt! Cupiditate minima animi illum. Culpa ea eum consequatur illum perferendis.
        """
    },

     {
        'id': 4,
        'name': 'Justin Biber Tour',
        'location': 'USA, Texas',
        'date': date(2021, 7, 20),
        'registered': 500,
        'organizer': 'Mike',
        'detail': """
            Nullam cursus iaculis erat ut eleifend. Sed metus quam, consectetur at tellus sit amet, consectetur tristique ipsum. Ut quis elementum augue. Nullam at volutpat nunc. Sed non velit luctus, sollicitudin urna eu, sagittis tellus. Vivamus tortor diam, vulputate sit amet vestibulum eu, porttitor in velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Etiam in sagittis magna. Etiam sodales elementum nulla, et hendrerit neque facilisis sed. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nunc congue imperdiet iaculis. Ut sed lorem arcu. Nam egestas orci nec tortor maximus, eu auctor nibh lacinia.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo expedita veritatis nostrum, sint perspiciatis numquam quod error hic suscipit velit aliquam ullam at natus alias, quam itaque rerum, facilis consequatur.

            Etiam vel metus eget ex convallis mollis vehicula vel est. Sed eleifend semper ligula, non efficitur nulla. Pellentesque ipsum nisl, fringilla nec massa et, bibendum vehicula est. Curabitur nulla sem, malesuada ut elit vitae, porta mattis lacus. Suspendisse volutpat magna sit amet lorem volutpat posuere. Proin dignissim enim elit, in semper lacus cursus sed. Morbi et accumsan augue, et scelerisque ligula. Praesent nisl erat, sollicitudin nec lacus eu, congue lacinia lectus. Duis varius aliquam arcu, nec accumsan erat interdum in. Cras eget finibus urna. Nullam condimentum at quam non ultricies. In convallis erat ac massa laoreet porta. Integer rutrum sagittis turpis nec dictum. Nulla convallis, nunc ut placerat pulvinar, lacus magna pharetra tellus, quis sagittis ante neque eu dolor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse tincidunt nunc lacus, non finibus augue pharetra quis.

            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Consequatur tempore, perspiciatis nostrum eaque quia magnam neque ad soluta? Adipisci, sunt! Cupiditate minima animi illum. Culpa ea eum consequatur illum perferendis.
        """
    }
]


def index(request):
    return render(request, 'events/index.html' )

def event_list(request):
    events = dummy_events
    return render(request, 'events/event_list.html' , {'events' : events})

def event_detail(request, id):
    event = None

    for e in dummy_events:
        if e['id'] == id:
            event = e
            break

    return render(request, 'events/event_detail.html' , {'event': event})