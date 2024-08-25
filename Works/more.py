def proverk_skvaziny(q_zhidk, rpr_nd, rzab):
  """
  Функция для проверки показаний работы скважины.

  Args:
    q_zhidk: Показания по снижению Qжидк.
    rpr_nd: Показания по увеличению Рпр(Нд).
    rzab: Показания по увеличению Рзаб.

  Returns:
    Инструкции по дальнейшим действиям.
  """

  # Проверка изменения показаний
  if q_zhidk and rpr_nd and rzab:
    print("Показания работы скважины изменились.")
    # Проверка устьевой арматуры
    proverk_ust_armatury()
  else:
    print("Показания работы скважины не изменились.")

def proverk_ust_armatury():
  """
  Функция для проверки устьевой арматуры.

  Returns:
    Инструкции по дальнейшим действиям.
  """
  # Проверка работоспособности ЗКЛ, ОК, при наличии ШДР
  # (заменить на реальную проверку)
  print("Проверка устьевой арматуры...")
  ust_armatura_ispravna = True  # (заменить на реальный результат)

  if ust_armatura_ispravna:
    print("Устьевая арматура исправна.")
    zamer_ust_davleniy()
  else:
    print("Устьевая арматура неисправна. Необходимо провести ремонт.")

def zamer_ust_davleniy():
  """
  Функция для замера устьевых давлений.

  Returns:
    Инструкции по дальнейшим действиям.
  """
  # Проверка Рб (заменить на реальный результат)
  rb = 100  # (заменить на реальное значение)
  kollektornoe_davlenie = 90  # (заменить на реальное значение)

  if rb > kolektornoe_davlenie:
    print("Рб выше коллекторного давления.")
    sostavlenie_zayavki_na_kislotnuyu_obrabotku()
  else:
    print("Замер устьевых давлений - Рб равно коллекторному давлению.")
    su_uetsn_s_chastotnym_preobrazovatelem()

def sostavlenie_zayavki_na_kislotnuyu_obrabotku():
  """
  Функция для составления заявки на кислотную обработку коллектора.
  """
  print("Составление, утверждение заявки на проведение кислотной обработки коллектора от устья СКВ до АГЗУ")

def su_uetsn_s_chastotnym_preobrazovatelem():
  """
  Функция для СУ УЭЦН с частотным преобразователем.
  """
  print("СУ УЭЦН с частотным преобразователем")

# Пример использования функций
proverk_skvaziny(True, True, True)  # Все показания изменились
proverk_skvaziny(True, False, False)  # Только Qжидк изменилось
proverk_skvaziny(False, True, False)  # Только Рпр(Нд) изменилось
proverk_skvaziny(False, False, True)  # Только Рзаб изменилось
