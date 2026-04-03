cmake_minimum_required(VERSION 3.14)
project(CSES_AutoTest)

# 1. C++ Standard festlegen
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 2. Google Test (gTest) automatisch einbinden
include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/refs/heads/main.zip
        DOWNLOAD_EXTRACT_TIMESTAMP TRUE
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

# 3. KATEGORIEN AUTOMATISCH FINDEN (Nie wieder händisch eintragen!)
file(GLOB CATEGORY_PATHS RELATIVE "${CMAKE_CURRENT_SOURCE_DIR}/src" "${CMAKE_CURRENT_SOURCE_DIR}/src/*")
set(CSES_CATEGORIES "")
foreach(path ${CATEGORY_PATHS})
    if(IS_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/src/${path}")
        list(APPEND CSES_CATEGORIES "${path}")
    endif()
endforeach()

# 4. Automatischer Setup-Loop
foreach(category ${CSES_CATEGORIES})

    # Suche alle .cpp Dateien im src-Ordner
    file(GLOB PROBLEM_FILES "${CMAKE_CURRENT_SOURCE_DIR}/src/${category}/*.cpp")

    foreach(file ${PROBLEM_FILES})
        get_filename_component(problem_name ${file} NAME_WE)

        # Pfad zur erwarteten Test-Datei
        set(test_file "${CMAKE_CURRENT_SOURCE_DIR}/tests/${category}/${problem_name}_test.cpp")

        # Prüfen, ob die Test-Datei existiert
        if(EXISTS ${test_file})
            set(target_name "${problem_name}_test")

            add_executable(${target_name} ${file} ${test_file})

            target_compile_definitions(${target_name} PRIVATE RUNNING_TESTS)
            target_link_libraries(${target_name} GTest::gtest_main)

            set_target_properties(${target_name} PROPERTIES FOLDER "Tests/${category}")

            include(GoogleTest)
            gtest_discover_tests(${target_name})

            message(STATUS "[OK] Target erstellt: ${target_name}")
        else()
            message(WARNING "[FEHLER] Test-Datei nicht gefunden unter: ${test_file}")
        endif()

    endforeach()
endforeach()