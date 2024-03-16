// Vue.filter('currency', function() {

//})
Vue.component('price', {
  data: function() {
    return {
      // prefix: '$',
      // value: 23.34,
      // precision: 2
    }
  },
  props: {
    value: Number,
    prefix: {
      type: String,
      default: '$'
    },
    precision: {
      type: Number,
      default: 2
    },
    conversion: {
      type: Number,
      default: 1
    }

  },
  // pass as object , object can be more flexible or array['value', 'prefix', 'precision', 'conversion'],
  template: '<span>{{ this.prefix + Number.parseFloat(this.value * this.conversion).toFixed(this.precision) }}</span>'
});

Vue.component('product-list', {
  props: ['products', 'maximum'],
  template: `
<transition-group name="fade" tag="div" 
    @beforeEnter="beforeEnter"
    @enter="enter"
    @leave="leave">
  <div class="row d-none mb-3 align-items-center" 
       v-for="(item, index) in products" :key="item.id" 
       v-if="item.price<=Number(maximum)"
       :data-index="index">
    <div class="col-1 m-auto">
      <button class="btn btn-info" 
              @click="$emit('add', item)">+</button>
    </div>
    <div class="col-sm-4">
         <img class="img-fluid d-block" :src="item.image" :alt="name">
        </div>
        <div class="col">
          <h3 class="text-info">{{ item.name }}</h3>
          <p class="mb-0">{{ item.description }}</p>
          <div class="h5 float-right"> 
            <price :value="Number(item.price)"></price></div>   
        </div>
      </div>
   
</transition-group>
`,
  methods: {
    beforeEnter: function(el) {
           el.className='d-none'
         },
         enter: function(el) {
           var delay=el.dataset.index * 100;
           setTimeout(function() {
            el.className='row d-flex mb-3 align-items-center animated fadeInRight'
          }, delay);
         },
         leave: function(el) {
           var delay=el.dataset.index * 100;
           setTimeout(function() {
            el.className='row d-flex mb-3 align-items-center animated fadeOutRight'
          }, delay);
         },
  }
});


var app = new Vue({
      el: '#app',
      data: {
          inputWidth: 60,
          sliderStatus: false,
          labelArr: ['font-weight-bold', 'mr-2'],
          maximum: 99,
          products: null,
          cart: []
        },
       filters: {
         currency: function(value) {
           return '$' + Number.parseFloat(value).toFixed(2);
         }
       },
       computed:  {
         cartTotal: function() {
           let sum = 0;
           for (key in this.cart) {
             sum = sum + (this.cart[key].product.price * this.cart[key].qty);
           }
           return sum;
         },
          cartQty: function() {
           let qty = 0;
           for (key in this.cart) {
             qty = qty + this.cart[key].qty;
           }
           return qty;
          },
         sliderState: function () {
          return this.sliderStatus ? 'd-flex': 'd-none'
         }
       },
       methods: {

         addItem: function(product) {
           //this.cart.push(product);
          var whichProduct;
           var existing = this.cart.filter(function(item, index) {
             if (item.product.id == Number(product.id)) {
               whichProduct = index;
               return true;
             } else {
               return false;
             }
           });

         if (existing.length) {
          this.cart[whichProduct].qty++
    } else {
      this.cart.push({product: product, qty: 1})
        }
      },
         deleteItem: function(id) {
          if(this.cart[id].qty>1) {
            this.cart[id].qty--;
        } else {
          this.cart.splice(id, 1);
        }
      }
    },
  mounted: function() {
    fetch('https://hplussport.com/api/products/order/price')
    .then(response => response.json())
    .then(data => {
      this.products = data;
    })
  }
});
