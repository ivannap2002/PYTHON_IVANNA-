from django.http import HttpResponse, JsonResponse
import webbrowser

# Función para redireccionar a Google
def getGoogle(request):
    webbrowser.open("https://www.google.com")
    return HttpResponse("Redireccionando a Google...")

# Función para imprimir la serie de Fibonacci hasta 100
def getFibonacci(request):
    a, b = 0, 1
    fibonacci_series = []
    while a <= 100:
        fibonacci_series.append(a)
        a, b = b, a + b
    return JsonResponse(fibonacci_series, safe=False)

# Función para imprimir números primos hasta un límite dado
def getPrimes(request, limit):
    limit = int(limit)  # Convertir el parámetro limit a entero
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    return JsonResponse(primes, safe=False)

# Función de saludo
def saludo(request):
    return HttpResponse("Hola Mundo.")
