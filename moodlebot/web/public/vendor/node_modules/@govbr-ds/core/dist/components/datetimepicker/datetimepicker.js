import flatpickr from 'flatpickr'
const Brazilian = require('flatpickr/dist/l10n/pt').default.pt

/** Classe para instanciar um objeto BRDateTimePicker*/
class BRDateTimePicker {
  /**
   * Instancia do objeto
   * @param {string} name - Nome do componente em minúsculo
   * @param {object} component - Objeto referenciando a raiz do componente DOM
   * @param {string} config - atributo de configuração do componente
   */
  constructor(name, component, config) {
    this.name = name
    this.component = component
    // localization global
    flatpickr.localize(Brazilian)

    this.configAttribute = this.component.getAttribute('datetimepicker-config')

    if (this.configAttribute) {
      // Transforma o atributo em um objeto
      const properties = this.configAttribute.split(',')
      this.obj = []
      properties.forEach((element) => {
        const tup = element.split(':')
        this.obj[tup[0]] = tup[1].replaceAll("'", '').trim() // eslint-disable-line

        this.saida = this.obj
      }, this)

      this.config = this.obj
    } else {
      this.config = config
    }

    this._buildDateTimePicker()
  }

  /**
   * Formata o componente e monta instância flatpickr
   * @private
   */
  _buildDateTimePicker() {
    let format = 'd/m/Y'
    let time = false
    let noCalendar = false
    switch (this.component.getAttribute('data-type')) {
      case 'date':
        format = 'd/m/Y'
        time = false
        noCalendar = false
        break
      case 'time':
        format = 'H:i'
        time = true
        noCalendar = true
        break
      case 'datetime-local':
        format = 'd/m/Y H:i'
        time = true
        noCalendar = false
        break
      default:
        format = 'd/m/Y'
        time = false
        noCalendar = false
        break
    }

    this.config_native = {
      dateFormat: format,
      disableMobile: 'true',
      enableTime: time,
      minuteIncrement: 1,

      mode: this.component.getAttribute('data-mode'),
      nextArrow:
        '<button class="br-button circle small" type="button"><i class="fas fa-chevron-right"></i></button>',
      noCalendar: noCalendar,
      prevArrow:
        '<button class="br-button circle small" type="button"><i class="fas fas fa-chevron-left"></i></button>',
      time_24hr: true,
      wrap: true,
      
    }
    this.config_flatpick = Object.assign(this.config, this.config_native)

    this.calendar = flatpickr(
      this.component,
      Object.assign(this.config, this.config_native)
    )

    

    this.calendar.config.onOpen.push(function() {
      document.querySelectorAll(".arrowUp").forEach(function(element){
        element.classList.add("fas", "fa-chevron-up");
      });
      document.querySelectorAll(".arrowDown").forEach(function(element){
        element.classList.add("fas", "fa-chevron-down");
      });
     } );
  }
}

export default BRDateTimePicker
